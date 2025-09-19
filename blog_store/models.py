from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog/previews/', null=True, blank=True, verbose_name="Превью")
    creation_at = models.DateField(auto_now_add=True)
    publication_sign = models.BooleanField(default=False, verbose_name="Опубликовано")
    number_views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "<Блоговая запись>"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-creation_at"]


