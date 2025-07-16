from itertools import product

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView,  ProductListView, ProductCreateView
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_inf/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create', ProductCreateView.as_view(), name='product_create')
]