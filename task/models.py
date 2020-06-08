from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    title = models.CharField(_('Title'), max_length=200,)
    text = models.TextField()
    is_done = models.BooleanField(default=False,)
    is_archive = models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return '{} : {}'.format(str(self.id), self.title)
    