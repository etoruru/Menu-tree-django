from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:menu_id>/', views.menuItems),
    path('menu/<int:menu_id>/<int:menu_item_id>', views.filter_items)
]