from django.urls import path

#import views

from . import views

urlpatterns = [
    path('', views.customers, name='customers'),\
    path('test/', views.test, name='test')
]