from django import template
from django.utils import timezone
register = template.Library()


@register.simple_tag
def permission(birth_date):
    diff = timezone.now().year - birth_date
    return 'allowed' if diff > 13 else 'blocked'


@register.simple_tag
def bizz_fuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'BizzFuzz'

    elif number % 3 == 0:
        return 'Bizz'

    elif number % 5 == 0:
        return 'Fuzz'
