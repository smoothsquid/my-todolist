from django.contrib.auth.models import AnonymousUser
from django.test import TestCase

from account.models import User, UserFactory
from .models import Task, get_max_order_num

class TaskModelTests(TestCase):

    def test_get_max_order_num(self):
        test_user = UserFactory.create_test_user(self)

        max_order = get_max_order_num(test_user)
        self.assertEqual(max_order, -1)

        Task.objects.create(author=test_user, title='제목1', order_num=0)

        max_order = get_max_order_num(test_user)
        self.assertEqual(max_order, 0)

        Task.objects.create(author=test_user, title='제목2', order_num=2)
        max_order = get_max_order_num(test_user)
        self.assertEqual(max_order, 2)
        Task.objects.create(author=test_user, title='제목3', order_num=3)
        
        max_order = get_max_order_num(test_user)
        self.assertEqual(max_order, 3)

    def test_task_re_order(self):
        test_user = UserFactory.create_test_user(self)
        task = Task.objects.create(author=test_user, title='제목1', order_num=0)
        task.order_num = 99
        task.save()

        task = Task.objects.get(pk=task.pk)

        self.assertEqual(task.order_num, 99)

    def test_task_re_order_function(self):
        test_user = UserFactory.create_test_user(self)
        task = Task.objects.create(author=test_user, title='제목1', order_num=0)
        Task.objects.create(author=test_user, title='제목2', order_num=2)
        Task.objects.create(author=test_user, title='제목3', order_num=3)
        Task.objects.create(author=test_user, title='제목4', order_num=4)

        task.update_order


    def test_create_test_user(self):
        test_user = UserFactory.create_test_user(self)
        print(test_user)
    