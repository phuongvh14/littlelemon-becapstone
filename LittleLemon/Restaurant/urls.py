from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('menu/item/<int:pk>', views.display_menu_item, name='menu_item'),
    path('book/', views.book, name="book"),
]
