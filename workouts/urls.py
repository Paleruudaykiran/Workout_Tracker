"""workouts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django import urls
from django.contrib import admin
from django.urls import path,include
import myapp
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static 
from django.conf import settings 
from myapp import views as myapp_views 
from django.views.static import serve 
# from django.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('forum/',myapp_views.forum,name='forum'),
    path('room/<str:pk>/',myapp_views.room,name='room'),
    path('create_room',myapp_views.create_room,name='create_room'),
    path('delete_room/<str:pk>/',myapp_views.delete_room,name='delete_room'),
    path('delete_message/<str:pk>/',myapp_views.delete_message,name='delete_message'),
    path('update_room/<str:pk>/',myapp_views.update_room,name='update_room'),
    path('update_msg/<str:pk>/',myapp_views.update_msg,name='update_msg'),
    path('challenges/',myapp_views.challenges,name='challenges'),
    path('goals/',myapp_views.goals,name='goals'),
    path('delete_goal/<str:pk>/',myapp_views.delete_goal,name='delete_goal'),
    path('participate_challenge/<str:pk>/',myapp_views.participate_challenge,name='participate_challenge'),
    path('challenge_completed/<str:pk>/',myapp_views.challenge_completed,name='challenge_completed'),
    path('create_challenge',myapp_views.create_challenge,name='create_challenge'),
    path('challenge_delete/<str:pk>/',myapp_views.challenge_delete,name='challenge_delete'),
    path('challenge_update/<str:pk>/',myapp_views.challenge_update,name="challenge_update"),
    path('category/<str:pk>/',myapp_views.workouts,name='workouts'),
    #  url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

