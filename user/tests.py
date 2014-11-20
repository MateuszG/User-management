from django.test import TestCase
from django.core.urlresolvers import reverse

from user.models import User
from user.forms import AddUserForm


class ViewTests(TestCase):

    def test_detail_view(self):
        user = User.objects.create(
            birthday='2000-12-12', email='a@o2.pl', username='a')
        response = self.client.get(reverse('user:detail', args=(user.pk,)))
        self.assertContains(response, user.email, status_code=200)

    def test_index_view(self):
        user1 = User.objects.create(
            birthday='2000-12-12', email='a@o2.pl', username='test')
        user2 = User.objects.create(
            birthday='2000-12-12', email='b@o2.pl', username='pytest')
        response = self.client.get(reverse('user:index'))
        self.assertContains(response, user1.username, status_code=200)
        self.assertContains(response, user2.username, status_code=200)

    def test_add_view(self):
        response = self.client.post(
            reverse('user:add'),
            {
                'username': "test",
                'email': 'b@o2.pl',
                'birthday': '2000-12-12',
                'password': 'test'
            }
        )
        self.assertEqual(response.status_code, 302)

    def test_edit_view(self):
        user = User.objects.create(
            birthday='2000-12-12', email='a@o2.pl', username='a')
        response = self.client.post(
            reverse('user:edit', kwargs={'pk': user.id}),
            {
                'username': "test",
                'email': 'a@o2.pl',
                'birthday': '2000-12-12',
                'password': 'test'
            }
        )
        self.assertEqual(response.status_code, 302)
