from django import forms
from .models import Human, Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model= Todo
        fields=('text', 'created', 'dueon', 'owner', 'mark')
