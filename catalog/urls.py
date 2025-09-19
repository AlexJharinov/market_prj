from itertools import product

from django.urls import path

from blog_store.views import BlogDetailView, BlogListView
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductListView, ProductCreateView, ProductEditView, ProductDeleteView
from catalog.views import contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_inf/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path("product/<int:pk>/edit/", ProductEditView.as_view(), name="product_edit"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]