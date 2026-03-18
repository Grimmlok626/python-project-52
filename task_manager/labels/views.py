from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .models import Label
from .forms import LabelForm

class LabelListView(LoginRequiredMixin, generic.ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'

class LabelCreateView(LoginRequiredMixin, generic.CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно создана')
        return response

class LabelUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    
    def test_func(self):
        return self.request.user.is_authenticated
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Метка успешно изменена')
        return response

class LabelDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('labels:list')
    
    def test_func(self):
        return self.request.user.is_authenticated
    
    def delete(self, request, *args, **kwargs):
        label = self.get_object()
        if label.tasks.exists():
            messages.error(request, 'Невозможно удалить метку')
            return redirect('labels:list')
        messages.success(request, 'Метка успешно удалена')
        return super().delete(request, *args, **kwargs)
