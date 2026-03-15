from django import forms
from ..models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {'name': 'Имя'}
        error_messages = {
            'name': {
                'unique': 'Этот статус уже существует',
                'required': 'Обязательное поле',
            },
        }