from django import template
from django.shortcuts import get_object_or_404
from Menu.models import *

register = template.Library()


@register.inclusion_tag('Tag_Menu.html')
def draw_menu(main_menu='Menu'):
    menu = get_object_or_404(ModelMenu, name=main_menu)

    children = []

    for i in ModelMenu.objects.all():
        if i.parent == menu:
            children.append(i)
    parents = []

    def find_parent(current_menu):
        parent = current_menu.parent
        parents.append(parent)
        if parent.parent != None:
            find_parent(parent)

    if menu.parent != None:
        find_parent(menu)

    return {'menu': menu, 'children': children, 'parents': parents}
