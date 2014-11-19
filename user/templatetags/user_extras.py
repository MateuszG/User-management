from django import template

register = template.Library()


@register.filter(name='permission')
def permission(years):
    return 'allowed' if years > 13 else 'blocked'


@register.filter(name='bizz_fuzz')
def bizz_fuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'BizzFuzz'

    elif number % 3 == 0:
        return 'Bizz'

    elif number % 5 == 0:
        return 'Fuzz'
