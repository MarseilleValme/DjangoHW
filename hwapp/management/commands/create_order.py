from django.core.management.base import BaseCommand
from hwapp.models import Order, Product, Client


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=2).first()
        print(client)
        product1 = Product.objects.filter(pk=4).first()
        print(product1)
        product2 = Product.objects.filter(pk=7).first()
        print(product2)
        total_price = product1.price + product2.price
        order = Order.objects.create(client=client, total_price=total_price)
        order.products.add(product1, product2)
        self.stdout.write(f'{order.id}')

        # customer = models.ForeignKey(Client, on_delete=models.CASCADE)
        # products = models.ManyToManyField(Product)
        # total_price = models.DecimalField(max_digits=8, decimal_places=2)
        # date_placing = models.DateTimeField(auto_now_add=True)