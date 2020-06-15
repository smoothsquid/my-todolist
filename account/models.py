import string, random

from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _


from task.models import Task

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError(_('Users must have an username'))

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin

class UserFactory:

    def create_test_user(self):
        username =  random_str(9) + random_num(4)
        password = random_str(5) + random_num(5)
        email = ''.join((random_str(4), random_num(2), '@', random_str(4), '.com',))
        return User.objects.create_user(username, email, password)

def random_str(size):
    return ''.join(random.sample(string.ascii_lowercase, size))

def random_num(size):
    return ''.join(random.sample(''.join(str(x) for x in range(0, 10)), 4))
