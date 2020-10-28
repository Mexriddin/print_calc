# from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
# Create your views here.


class OrdersView(ListView):
    model = Order
    queryset = Order.objects.all().order_by("-date_created")
    template_name = 'orders/orders.html'
    context_object_name = 'orders'


class OrderCreateView(CreateView):
    model = Order
    template_name = 'orders/order_new.html'
    fields = ['client_name', 'client_phone', 'client_company', 'count', 'paper', 'devision_paper', 'print_paper']


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'orders/order_edit.html'
    fields = ['client_name', 'client_phone', 'client_company', 'count', 'paper', 'devision_paper', 'print_paper']


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_delete.html'
    success_url = reverse_lazy('home')
