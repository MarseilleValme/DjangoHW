from django.contrib import admin
from .models import Category, Product, Client, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_reg', 'is_deleted']
    # name = models.CharField(max_length=100)
    # email = models.EmailField()
    # phone = models.IntegerField()
    # address = models.CharField(max_length=100)
    # date_reg = models.DateField(auto_now_add=True)
    # is_deleted = models.BooleanField(default=False)


class OrderAdmin(admin.ModelAdmin):
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # products = models.ManyToManyField(Product)
    # total_price = models.DecimalField(max_digits=8, decimal_places=2)
    # date_placing = models.DateField(auto_now_add=True)

    list_display = ['client', 'total_price', 'date_placing']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['created_at', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю "Описание продукта" (description)'
    actions = ['reset_quantity']
    # fields = ['name', 'description', 'category', 'created_at']
    readonly_fields = ['created_at']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields':['category', 'description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]

    @admin.action(description="Сбросить количество в ноль")
    def reset_quantity(self, request, queryset):
        queryset.update(quantity=0)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)