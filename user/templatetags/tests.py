from django.test import TestCase
from django.core.urlresolvers import reverse

from user.templatetags.user_extras import bizz_fuzz
from user.models import User


class TagsTests(TestCase):

    def test_bizz_fuzz(self):
        self.assertEqual(bizz_fuzz(15), 'BizzFuzz' )
        self.assertEqual(bizz_fuzz(5), 'Fuzz' )
        self.assertEqual(bizz_fuzz(3), 'Bizz' )
        self.assertEqual(bizz_fuzz(4), 4)
