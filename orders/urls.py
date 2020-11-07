from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
   # path("", OrdersView.as_view(), name='home'),
   path("", OrderList, name='home'),
   # path("order/new", OrderCreateView.as_view(), name='order_new'),
   path("order/new", OrderCreate, name='order_new'),
   # path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
   path('order/<int:pk>/edit/', OrderUpdate, name='order_edit'),
   # path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
   path('order/<int:pk>/delete/', OrderDelete, name='order_delete'),
   path('user/', userPage, name='user-page'),

]


