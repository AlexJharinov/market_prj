from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHES_ENABLED


def get_product_from_cache():
    """
        Получает данные по продуктам из кэша если кэш пуст берет данные из БД.
    """
    if not CACHES_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

from django.shortcuts import get_object_or_404
from catalog.models import Category, Product

def get_products_by_category_id(category_id: int, published_only: bool = True):
    """
    Вернёт (category, queryset) для всех продуктов указанной категории по её id.
    """
    category = get_object_or_404(Category, pk=category_id)

    queryset = (
        Product.objects
        .select_related("category", "owner")
        .filter(category=category)
        .order_by("-created_at", "-id")
    )
    if published_only:
        queryset = queryset.filter(publication_sign=True)
    return category, queryset
