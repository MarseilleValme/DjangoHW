from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='base'),
    path('about/', views.about, name='about'),
    path('create_client/', views.create_client, name='create_client'),
    path('all_clients/', views.all_clients_view, name='all_clients'),
    path('create_product/', views.create_product, name='create_product'),
    path('all_products/', views.all_products, name='all_products'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('clients/<int:client_id>/update/', views.update_client, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client, name='delete_client'),
    path('clients/<int:client_id>/ordered_products/<int:days>/', views.client_ordered_products,
         name='client_ordered_products'),
]