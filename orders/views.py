from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import allowed_users, admin_only
from .forms import *


# Create your views here.


""" Page for users """
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = Order.objects.all().order_by("-date_created")
    contex = {'orders': orders}

    return render(request, 'orders/user.html', contex)


""" Orders """
@login_required(login_url='login')
@admin_only
def OrderList(request):
    orders = Order.objects.all().order_by("-date_created")
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context)


""" Order Create """
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


""" Order Update """
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


""" Order Delete """
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def OrderDelete(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {"order": order}
    return render(request, 'orders/order_delete.html', context)
