from django import template

register = template.Library()


@register.filter(name="sum")
def cut(value):
    return sum(value)
