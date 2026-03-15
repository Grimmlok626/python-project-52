from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from ..models import Task
from .forms import TaskForm

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Можно фильтровать, например, только свои задачи или все
        return Task.objects.all()

class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Задача успешно создана')
        return response

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Задача успешно изменена')
        return response

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:list')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.author

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Задача успешно удалена')
        return super().delete(request, *args, **kwargs)