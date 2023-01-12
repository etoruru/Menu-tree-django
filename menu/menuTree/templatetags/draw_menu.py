from django import template

register = template.Library()

@register.simple_tag
def return_name(name):
    return name