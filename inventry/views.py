from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'dashboard/index.html', context)

def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    items = Product.objects.all()
    order = Order.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added.')
            return redirect('dashboard-product')

    else:
        form = ProductForm()    

    context = {
        'items' : items,
        'form' : form,  
        'order':order,   
    }
    return render(request, 'dashboard/product.html', context)  

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')    

def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
            
    else:
        form = ProductForm(instance=item)

    context= {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)          

def order(request):
    orders = Order.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard-order')
    else:
        form = OrderForm() 

    context = {
        'orders': orders,
        'form': form,
    }
    return render(request, 'dashboard/order.html', context)    