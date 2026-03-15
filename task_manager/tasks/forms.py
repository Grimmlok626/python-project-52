from django import forms
from ..models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assigned_to']
        labels = {
            'name': 'Имя',
            'description': 'Описание',
            'status': 'Статус',
            'assigned_to': 'Исполнение',
        }
        error_messages = {
            'name': {
                'unique': 'Такая задача уже существует',
                'required': 'Обязательное поле',
            },
        }
