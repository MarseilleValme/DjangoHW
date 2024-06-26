from django.core.management.base import BaseCommand
from hwapp.models import Client


class Command(BaseCommand):
    help = "Delete user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.is_deleted = True
            client.save()
        self.stdout.write(f'{client}')