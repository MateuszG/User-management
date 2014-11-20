import csv

from django.http import (
    HttpResponseRedirect,
    HttpResponse
)
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import FormView
from django.shortcuts import (
    render,
    get_object_or_404
)
from user.forms import AddUserForm
from user.models import User
from user.templatetags.user_extras import (
    permission,
    bizz_fuzz
)


class IndexUsersView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)


class DetailUserView(generic.DetailView):
    model = User
    template_name = 'user/detail.html'


class AddUserView(FormView):
    form_class = AddUserForm
    template_name = 'user/add.html'
    success_url = reverse_lazy('user:index')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


class EditUserView(generic.UpdateView):
    model = User
    template_name = 'user/edit.html'
    fields = ['username', 'email', 'password', 'birthday']

    def get_success_url(self):
        return reverse_lazy('user:detail', args=(self.object.pk,))


class DeleteUserView(generic.DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user:index')


def generate_cvs(request):
    all_users = User.objects.filter(is_staff=False)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])

    for user in all_users:
        eligible = permission(user.get_year())
        bizzfuzz = bizz_fuzz(user.number)
        writer.writerow(
            [user.username, user.birthday, eligible, user.number, bizzfuzz]
        )

    return response
