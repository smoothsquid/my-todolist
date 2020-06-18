"""

    인증에 필요한 사용자와 UserManager를 정의합니다.

"""
import string
import random
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """
    사용자를 생성합니다.
    """

    def create_user(self, username, email, password=None):
        """
        일반 사용자를 생성합니다.
        """
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
        """
        Staff 사용자를 생성합니다.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    할일 관리 서비스를 이용하는 사용자 입니다.
    """
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
        """
        사용자가 권한을 가지고 있는지 반환 합니다. 필요에 따라 추후 구현합니다.
        """
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        """
        해당 사용자가 관리자(staff)인지 반환합니다. 
        """
        return self.is_admin

class UserFactory:
    """
    테스트를 위한 사용자나 특수한 목적으로 필요한 사용자를 미리 정의해두고 생성합니다.
    """

    def create_test_user(self):
        """
        모든 값을 랜덤으로 갖는 사용자를 생성합니다.
        테스트 환경에서만 실행해야합니다.
        """
        username =  random_str(9) + random_num(4)
        password = random_str(5) + random_num(5)
        email = ''.join((random_str(4), random_num(2), '@', random_str(4), '.com',))
        return User.objects.create_user(username, email, password)

def random_str(size):
    """
    원하는 길이의 임의 문자열을 반환합니다.
    """
    return ''.join(random.sample(string.ascii_lowercase, size))

def random_num(size):
    """
    숫자로 이루어진 원하는 길이의 문자열을 반환합니다.
    """
    return ''.join(random.sample(''.join(str(x) for x in range(0, 10)), size))
