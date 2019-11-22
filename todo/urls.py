from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from todo.views import index
from . import views

urlpatterns = [
    path('', index, name="index"),
    #url(r'^todos/$', views.all_todo, name='all_todo'),
	path('todo/<int:pk>/', views.det.as_view(), name='det')
]