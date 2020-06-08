from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase

from .models import Task

class TaskModelTests(TestCase):

    def test_get_max_order_num(self):
        user = User.objects.create_user('user1', email='user@user.com', password='1234a')
        Task.objects.create(author=user, title='제목1', order_num=0)
        Task.objects.create(author=user, title='제목2', order_num=2)
        Task.objects.create(author=user, title='제목3', order_num=3)
        
        tasks = Task.objects.filter(author=user)
        max_order = max(list(map(lambda x: x.order_num, tasks)))
        self.assertEqual(max_order, 3)
    