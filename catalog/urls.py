from itertools import product

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import base, product_detail
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('contacts/', contacts, name='contacts'),
    path('product_inf/<int:pk>/', product_detail, name='product_detail'),


]