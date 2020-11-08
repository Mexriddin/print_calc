from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   path("", OrderList, name='home'),
   path("order/new", OrderCreate, name='order_new'),
   path('order/<int:pk>/edit/', OrderUpdate, name='order_edit'),
   path('order/<int:pk>/delete/', OrderDelete, name='order_delete'),
   path('user/', userPage, name='user-page'),
]


