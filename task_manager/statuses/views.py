from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from task_manager.models import Status
from .forms import StatusForm
from task_manager.models import Task  # предположим, у вас есть модель Task

class StatusListView(LoginRequiredMixin, generic.ListView):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'

class StatusCreateView(LoginRequiredMixin, generic.CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('statuses:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно создан')
        return response

    def form_invalid(self, form):
        # Дополнительно — обработка ошибок
        if 'already exists' in str(form.errors):
            form.add_error('name', 'Этот статус уже существует')
        return super().form_invalid(form)

class StatusUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('statuses:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Статус успешно изменен')
        return response

    def form_invalid(self, form):
        if 'already exists' in str(form.errors):
            form.add_error('name', 'Этот статус уже существует')
        return super().form_invalid(form)

class StatusDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Status
    template_name = 'statuses/status_confirm_delete.html'
    success_url = reverse_lazy('statuses:list')

    def delete(self, request, *args, **kwargs):
        status = self.get_object()
        if status.task_set.exists():
            messages.error(request, 'Невозможно удалить статус, связанный с задачами')
            from django.shortcuts import redirect
            return redirect('statuses:list')
        response = super().delete(request, *args, **kwargs)
        messages.success(request, 'Статус успешно удален')
        return response