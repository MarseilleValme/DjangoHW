from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    date_reg = models.DateField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}, ' \
               f'date_reg: {self.date_reg}, deleted: {self.is_deleted}'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (
            f'Product: {self.name}, description: {self.description}, price:{self.price}, rest_quantity:{self.quantity}, '
            f'created_at:{self.created_at}')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_placing = models.DateField(auto_now_add=True)

    def __str__(self):
        product_names = ', '.join([product.name for product in self.products.all()])
        return (f'Order details: Client name: {self.client.name}, client phone: {self.client.phone},'
                f' goods in order: {product_names}, '
                f'total price: {self.total_price}')
