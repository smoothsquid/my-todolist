from django.forms import ModelForm, TextInput
from task.models import Task

class SimpleTaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            'title': TextInput(attrs={'placeholder': '할일'})
        }
        labels = {
            'title': ''
        }
