from django.urls import path

#import views

from . import views

urlpatterns = [
    path('', views.purchases, name='purchases'),\
    path('new_purchase/', views.new_purchase, name="new_purchase"),\
]