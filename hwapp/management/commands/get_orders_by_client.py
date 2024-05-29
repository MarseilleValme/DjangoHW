from django.core.management.base import BaseCommand
from hwapp.models import Client, Order


class Command(BaseCommand):
    help = "Get all orders by client id."

    # def add_arguments(self, parser):
    #     parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # pk = kwargs.get('pk')
        pk = 2
        client = Client.objects.filter(pk=pk).first()
        # if client is not None:
        orders = Order.objects.filter(client=client)
        print(orders)
        intro = f'All orders of {client.name}\n'
        text = '\n'.join(order.products for order in orders)
        self.stdout.write(f'{intro}{text}')
