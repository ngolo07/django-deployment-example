from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    when the function cut is called as a filter, it will be cut:'value', we want whatever is passed to it to be removed

    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')

"""
from django import template

register = template.Library()

@register.filter(name='cut')
def cu(value, arg):
return value.replace(arg, '')
"""