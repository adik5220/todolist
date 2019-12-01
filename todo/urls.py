from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from todo.views import index
from . import views

urlpatterns = [
    path('todo/', index, name="index"),
    path('todo/contact/', views.contact, name="contact"),
    path('todo/all/', views.all.as_view(), name='all'),
	path('todo/<int:pk>/', views.det.as_view(), name='det')
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]