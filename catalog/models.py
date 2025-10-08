from django.db import models

from users.models import User



class Category(models.Model):
    """
        Класс Category
    """
    name_category = models.CharField(max_length=150, verbose_name="Категория")
    desc_category = models.TextField(null=True)

    def __str__(self):
        """
            Магические метод вызывает строчное название Категории
        """
        return f"{self.name_category}"

    class Meta:
        """
        Класс задет имя модели
        """
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    """
    Класс продукты
    """
    name_product = models.CharField(max_length=150, verbose_name="Продукт")
    desc = models.TextField(null=True, blank=True, verbose_name="Описание")
    image = models.ImageField(null=True, blank=True, upload_to="catalog/photos", verbose_name="Фотография")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    p_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    created_at = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    publication_sign = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец'
    )

    def __str__(self):
        """
            Задает строчное представление для класса Продукты
        """
        return f"{self.name_product} {self.category}"

    class Meta:
        """
            Настройки класса для новых функций класса продукты
        """
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["p_price"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
            ("can_delete_product", "Может удалять продукты других пользователей"),
        ]



