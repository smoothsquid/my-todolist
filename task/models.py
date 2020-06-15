from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def get_max_order_num(user):
    tasks = Task.objects.filter(author=user)
    if not tasks:
        return - 1
    return max(list(map(lambda x: x.order_num, tasks)))

class Task(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    title = models.CharField(_('Title'), max_length=200,)
    text = models.TextField()
    is_done = models.BooleanField(default=False,)
    is_archive = models.BooleanField(default=False,)
    created = models.DateTimeField(auto_now=True,)
    order_num = models.IntegerField()

    def __str__(self):
        return '{} : {}'.format(str(self.pk), self.title)

    # 해당 Task의 순서를 변경합니다.
    def update_order(self, order):
        if self.order_num is order:
            return
        origin_order = self.order_num
        self.order_num = order
        new_order_gt = order > origin_order
        
        tasks = Task.objects.filter(author=self.author)
        for task in tasks:
            if new_order_gt:
                task.order_num = task.order_num - 1
            else:
                task.order_num = task.order_num + 1
            task.save()

        return

    # 특정 회원의 Task를 모두 불러와서 재 정렬합니다.
    def re_order(self):
        pass
    