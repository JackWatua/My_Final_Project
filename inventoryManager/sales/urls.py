from django.urls import path

#import views

from . import views

urlpatterns = [
    path('', views.sales, name='sales'),\
    path('new_sale/', views.new_sale, name = 'new_sale'),\
]