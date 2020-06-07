from django import forms
from task.models import Task

class SimpleTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title',]
