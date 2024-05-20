import logging
from django.shortcuts import render
from django.utils import timezone
from .models import Order



logger = logging.getLogger(__name__)


def index(request):
    logger.info("Main page accessed")
    return render(request, 'index.html')


def about(request):
    logger.info("About me accessed")
    return render(request, 'about.html')


def client_ordered_products(request, client_id, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    orders = Order.objects.filter(client_id=client_id, date_placing__range=(start_date, end_date))

    ordered_products = []
    for order in orders:
        ordered_products.extend(order.products.all())

    uniq_ordered_products = list(set(ordered_products))

    context = {
        'client_id': client_id,
        'ordered_products': uniq_ordered_products,
        'days': days,
    }
    return render(request, 'client_ordered_products.html', context)