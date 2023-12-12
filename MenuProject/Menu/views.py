from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def menu_view(request, menu_name):
    menu = get_object_or_404(ModelMenu, name=menu_name)

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
    return render(request, 'menu.html', {'menu': menu, 'children': children, 'parents': parents})


def Main_page_view(request):
    all_menus = ModelMenu.objects.all()
    menus = []
    for i in all_menus:
        if not i.parent:
            menus.append(i)
    return render(request, 'MainPage.html', {'MainMenus': menus})
