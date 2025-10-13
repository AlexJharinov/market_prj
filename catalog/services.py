from django.core.cache import cache
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from catalog.models import Category, Product
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

def products_by_category_id(category_id: int, published_only: bool = True) -> QuerySet[Product]:
    """
    Возвращает QuerySet продуктов по ID категории.
    Если категории с таким ID нет — вернётся пустой QuerySet.
    """
    qs = (
        Product.objects
        .select_related("category", "owner")
        .filter(category_id=category_id)
        .order_by("-created_at", "-id")
    )
    return qs.filter(publication_sign=True) if published_only else qs
