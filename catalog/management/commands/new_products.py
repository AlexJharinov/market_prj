
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление новых продуктов в базу"

    def handle(self, *args, **options):
        category = Category.objects.get_or_create(name_category='Техника', desc_category='Все что нужно')


        product = [
            {'name_product': 'Телевзор', 'desc': '3 дюйма', 'category': category, 'p_price': '10'},
            {'name_product': 'Плеер', 'desc': 'Касетный', 'category': category, 'p_price': '100'},
                ]


        for product_data in product:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже добавлен'))
