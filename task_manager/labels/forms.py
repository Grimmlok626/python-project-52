from django import forms
from ..models import Label

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {'name': 'Имя'}
        error_messages = {
            'name': {
                'unique': 'Уже существует',
                'required': 'Обязательное поле'
            }
        }