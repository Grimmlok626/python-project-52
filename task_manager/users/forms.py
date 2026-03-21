from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля',
        }