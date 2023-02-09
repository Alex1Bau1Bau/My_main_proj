from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('jsproj', views.jsProj, name='jsproj'),

    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
]