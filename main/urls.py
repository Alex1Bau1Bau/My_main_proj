from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('jsproj', views.jsProj, name='jsproj'),
    path('news_pars_all', views.news_parsing_all, name='news_pars_all'),
    path('createarticles', views.create_articles, name='createarticles'),

    path('register', views.RegisterUser.as_view(), name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),

    path('myphoto', views.my_photo, name='myphoto'),
    path('myvideo', views.my_video, name='myvideo'),
    path('mymusic', views.my_music, name='mymusic'),
]