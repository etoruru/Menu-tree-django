from django import template

from ..models import MenuItem

register = template.Library()


@register.simple_tag
def return_children(active):
    children = MenuItem.objects.select_related('parent').filter(parent=active)
    return children
