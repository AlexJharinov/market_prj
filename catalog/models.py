from django.db import models

# Create your models here.

# Описание моделей:
# Product:
# наименование,
# описание,
# изображение,
# категория,
# цена за покупку,
# дата создания,
# дата последнего изменения.
# Category:
# наименование,
# описание.


class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name="Категория")
    desc_category = models.TextField(null=True)

    def __str__(self):
        return f"{self.name_category}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name="Продукт")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(null=True, blank=True, upload_to="catalog/photos", verbose_name="Фотография")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    p_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    created_at = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name_product} {self.category}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["p_price"]



