from random import randrange
from django.db.models import (
    DateField,
    IntegerField,
    CharField,
    EmailField,
    BooleanField,
    DateTimeField
)
from django.utils import timezone
from django.contrib.auth.models import(
    AbstractBaseUser,
    UserManager,
    PermissionsMixin
)


def my_random_key():
    return randrange(100)


class User(AbstractBaseUser, PermissionsMixin):
    username = CharField(max_length=20, unique=True)
    email = EmailField(max_length=254, unique=True)
    birthday = DateField(blank=False, null=False)
    number = IntegerField(blank=False, null=True, default=my_random_key)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username  # pragma: no cover

    def get_short_name(self):
        return self.email  # pragma: no cover

    def get_year(self):
        return self.birthday.year
