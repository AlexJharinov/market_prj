
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление новых продуктов в базу"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category = Category.objects.create(name_category='Техника', desc_category='Все что нужно')

        category_1 =  Category.objects.create(name_category='Одежда', desc_category='Носят люди')




        product = [
            {'name_product': 'Телевзор', 'desc': '3 дюйма', 'category': category, 'p_price': '10'},
            {'name_product': 'Плеер', 'desc': 'Касетный', 'category': category, 'p_price': '100'},
            {'name_product': 'Майка', 'desc': 'Красная', 'category': category_1, 'p_price': '100'},
            {'name_product': 'Носки', 'desc': 'Для четырех пальцев', 'category': category_1, 'p_price': '13'},
                ]


        for product_data in product:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт добавлен'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже добавлен'))
