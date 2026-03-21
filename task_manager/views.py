from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from task_manager.users.forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # или куда вы хотите после регистрации

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Вы успешно зарегистрировались!')
        return super().form_valid(form)