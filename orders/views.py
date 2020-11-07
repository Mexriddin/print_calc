from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import allowed_users, admin_only
from .forms import *

from django.contrib import messages
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = Order.objects.all().order_by("-date_created")
    contex = {'orders': orders}

    return render(request, 'orders/user.html', contex)





# Create your views here.

# class OrdersView(ListView):
#     model = Order
#     queryset = Order.objects.all().order_by("-date_created")
#     template_name = 'orders/orders.html'
#     context_object_name = 'orders'


@login_required(login_url='login')
@admin_only
def OrderList(request):
    orders = Order.objects.all().order_by("-date_created")
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context)

# class OrderCreateView(CreateView):
#     model = Order
#     template_name = 'orders/order_new.html'
#     fields = ['client_name', 'client_phone', 'client_company', 'count', 'paper', 'devision_paper', 'print_paper']

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def OrderCreate(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'orders/order_new.html', context=context)



# class OrderUpdateView(UpdateView):
#     model = Order
#     template_name = 'orders/order_edit.html'
#     fields = ['client_name', 'client_phone', 'client_company', 'count', 'paper', 'devision_paper', 'print_paper']
#



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def OrderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'orders/order_edit.html', context=context)


# class OrderDeleteView(DeleteView):
#     model = Order
#     template_name = 'orders/order_delete.html'
#     success_url = reverse_lazy('home')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def OrderDelete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {"order": order}
    return render(request, 'orders/order_delete.html', context)
