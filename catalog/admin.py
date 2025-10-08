from django.contrib import admin
from catalog.models import Category, Product



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
        Настройка отображения модели Category в административной панели Django
    """
    list_display = ('id', 'name_category',)
    list_filter = ('name_category',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
        Настройка отображения модели Product в административной панели Django
    """
    list_display = ('id','name_product', 'p_price', 'desc')
    list_filter = ('name_product', 'desc')
    search_fields = ('name_product', 'name_category', 'p_price')