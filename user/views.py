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
from django.views.generic.edit import FormView
from .forms import AddUserForm


class IndexUsersView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter()


class DetailUserView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'


class AddUserView(FormView):
    form_class = AddUserForm
    template_name = 'user/add.html'
    success_url = '/user/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class EditUserView(generic.DetailView):
    model = User
    template_name = 'user/results.html'


class DeleteUserView(generic.DetailView):
    model = User
    template_name = 'user/results.html'
