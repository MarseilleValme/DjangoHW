from django.core.management.base import BaseCommand
from hwapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Sergey', email='sergey@example.com', phone_number=987654321, adres='Kharkov', is_deleted = False)
        user.save()
        self.stdout.write(f'{user}')

    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone_number = models.IntegerField()
    # adres = models.CharField(max_length=100)
    # date_reg = models.DateTimeField(auto_now_add=True)
