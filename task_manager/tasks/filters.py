import django_filters
from django import forms
from .models import Task
from task_manager.models import Status, User, Label

class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label='Статус',
        queryset=Status.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    executor = django_filters.ModelChoiceFilter(
        label='Исполнитель',
        queryset=User.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    labels = django_filters.ModelChoiceFilter(
        label='Метка',
        queryset=Label.objects.all(),
        empty_label='Все',
        widget=forms.Select(attrs={'class': 'form-select'}),
        field_name='labels',
        method='filter_labels'
    )
    only_mine = django_filters.BooleanFilter(
        label='Только свои задачи',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        method='filter_only_mine'
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'only_mine']

    def filter_labels(self, queryset, name, value):
        if value:
            return queryset.filter(labels=value)
        return queryset

    def filter_only_mine(self, queryset, name, value):
        user = self.request.user
        if value and user.is_authenticated:
            return queryset.filter(author=user)
        return queryset