from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/<int:client_id>/ordered_products/<int:days>/', views.client_ordered_products,
         name='client_ordered_products'),
]