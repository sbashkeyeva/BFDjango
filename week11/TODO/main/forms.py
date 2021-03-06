from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name', 'created', 'dueon', 'owner', 'mark')


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('name', 'created', 'dueon', 'owner', 'mark')
