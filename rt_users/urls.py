from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from . import views

urlpatterns = [
    path('', views.profile_view, name='Profile_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),   
]