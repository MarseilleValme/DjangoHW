from django.core.management.base import BaseCommand
from hwapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='product1', description='description of product1', price=111, quantity='11')
        product.save()
        self.stdout.write(f'{product}')

        # name = models.CharField(max_length=100)
        # description = models.TextField()
        # price = models.DecimalField(max_digits=8, decimal_places=2)
        # quantity = models.IntegerField()
        # created_at = models.DateTimeField(auto_now_add=True)