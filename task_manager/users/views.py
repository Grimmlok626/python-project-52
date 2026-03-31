from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import RegisterForm


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('login')

def form_valid(self, form):
    response = super().form_valid(form)
    messages.success(self.request, 'Пользователь успешно зарегистрирован')
    return response


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:list')

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return super().handle_no_permission()


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:list')

    def test_func(self):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return super().handle_no_permission()