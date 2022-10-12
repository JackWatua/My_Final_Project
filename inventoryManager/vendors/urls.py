from django.urls import path

#import views

from . import views

urlpatterns = [
    path('', views.vendors, name='vendors'),\
    path('new_vendor/', views.new_vendor, name="new_vendor"),\
]