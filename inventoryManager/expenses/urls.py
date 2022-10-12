from django.urls import path

#import views

from . import views

urlpatterns = [
    path('', views.expenses, name='expenses'),\
    path('new_expense/', views.new_expense, name= "new_expense")
]