from django import forms
from .models import Client, Product


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone', 'address']
        # name = models.CharField(max_length=100)
        # email = models.EmailField()
        # phone = models.IntegerField()
        # address = models.CharField(max_length=100)
        # date_reg = models.DateField(auto_now_add=True)
        # is_deleted = models.BooleanField(default=False)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']
        # name = models.CharField(max_length=100)
        # description = models.TextField()
        # price = models.DecimalField(max_digits=8, decimal_places=2)
        # quantity = models.IntegerField()
        # created_at = models.DateField(auto_now_add=True)
        # image = models.ImageField(upload_to='images/', null=True, blank=True)
