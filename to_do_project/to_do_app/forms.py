from django.forms import ModelForm
from .models import ToDos

class ToDoForm(ModelForm):
    class Meta:
        model = ToDos
        fields = ['title', 'notes', 'important']