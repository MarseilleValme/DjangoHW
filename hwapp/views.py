import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Order, Client, Product
from .forms import ClientForm, ProductForm


logger = logging.getLogger(__name__)


def main(request):
    logger.info("Main page accessed")
    return render(request, 'base.html')


def about(request):
    logger.info("About me accessed")
    return render(request, 'about.html')


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'User not entered'
        if form.is_valid():
            form.save()
            return redirect('all_clients')
            message = 'User saved'
    else:
        form = ClientForm()
        message = 'Fill the form'
    return render(request, 'create_client.html', {'form': form,  'message': message})


def all_clients_view(request):
    clients = Client.objects.all()
    return render(request, 'all_clients.html', {'clients': clients})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('all_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('all_products')
    return render(request, 'confirm_delete_product.html', {'product': product})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


def update_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('all_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'update_client.html', {'form': form, 'client': client})


def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('all_clients')
    return render(request, 'delete_client.html', {'client': client})


def client_ordered_products(request, client_id, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    orders = Order.objects.filter(client_id=client_id, date_placing__range=(start_date, end_date))

    sorted_orders = sorted(orders, key=lambda x: x.date_placing, reverse=True)

    ordered_products = []
    for order in sorted_orders:
        ordered_products.extend(order.products.all())

    uniq_ordered_products = list(set(ordered_products))

    context = {
        'client_id': client_id,
        'ordered_products': uniq_ordered_products,
        'days': days,
    }
    return render(request, 'client_ordered_products.html', context)