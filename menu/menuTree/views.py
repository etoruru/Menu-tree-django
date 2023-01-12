from django.shortcuts import render
from django.http import HttpResponse

from .models import  MenuItem


# Create your views here.
def index(request):
    menu = MenuItem.objects.filter(level=0)
    output = {
        "menu" : menu
    }
    return render(request, 'menu.html', output)


def filter(request, menu_item_id):
    queryset = MenuItem.objects.select_related('parent')
    output = {
        "menu": queryset
    }
    return render(request, 'menu.html', output)