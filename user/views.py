from django.shortcuts import (
    render,
    get_object_or_404
)
from django.http import (
    HttpResponseRedirect
)
from django.core.urlresolvers import reverse

from .models import User
from django.views import generic
from django.utils import timezone


class IndexUsersView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter()


class DetailUserView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return User.objects.filter(pub_date__lte=timezone.now())


class AddUserView(generic.DetailView):
    pass
    # model = User
    # template_name = 'user/results.html'



class EditUserView(generic.DetailView):
    model = User
    template_name = 'user/results.html'


class DeleteUserView(generic.DetailView):
    model = User
    template_name = 'user/results.html'
