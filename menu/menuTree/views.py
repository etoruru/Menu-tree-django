from django.shortcuts import render

from .models import Menu,MenuItem


# Create your views here.
def index(request):
    menu = Menu.objects.all()
    output = {
        "menu": menu,
        "path": request.path
    }
    return render(request, 'index.html', output)


def menuItems(request, menu_id):
    menu = MenuItem.objects.filter(menu=menu_id, parent=None)
    output = {
        "active": menu,
        "path": request.path
    }
    return render(request, 'index.html', output)


def filter_items(request,menu_id, menu_item_id):
    active = MenuItem.objects.get(pk=menu_item_id)

    output = {
        "active": active,
        "path": request.path,
        "menu_id": menu_id
    }
    return render(request, 'menuItem.html', output)