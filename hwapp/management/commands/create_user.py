from django.core.management.base import BaseCommand
from hwapp.models import Client


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = Client(name='Zhora', email='zhora@example.com', phone=123456789, adres='Kharkov', is_deleted = False)
        client.save()
        self.stdout.write(f'{client}')

    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone = models.IntegerField()
    # adres = models.CharField(max_length=100)
    # date_reg = models.DateTimeField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)
