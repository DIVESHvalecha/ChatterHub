from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Main chat app URLs
    path('chat/<str:group_name>/', views.group, name="group"),  # Main chat app URLs
]