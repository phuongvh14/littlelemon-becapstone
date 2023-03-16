from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu-item-view'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-view'),
    path('api-token-auth/', obtain_auth_token)
]