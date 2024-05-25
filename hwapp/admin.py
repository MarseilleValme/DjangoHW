from django.contrib import admin
from .models import Category, Product


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(Modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['created_at', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю "Описание продукта" (description)'
    actions = [reset_quantity]
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


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

