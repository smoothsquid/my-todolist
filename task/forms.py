from django import forms
from task.models import Task
from django.utils.translation import ugettext_lazy as _

class SimpleTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': _('To Do')})
        }
        labels = {
            'title': ''
        }

class ChangeTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("title", "text",)
        labels = {
            'title': _('Title'),
            'text': _('Memo'),
        }
