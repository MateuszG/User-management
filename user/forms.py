from django.forms import ModelForm, DateInput
from django.contrib.admin import widgets
from user.models import User


class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'birthday',
        )
