from unicodedata import category

from django import forms
from .models import Product


words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

class ProductForm(forms.ModelForm):
    """
        Форма для создания и редактирования объектов модели Product.
    """
    class Meta:
        model = Product
        fields = ['name_product', 'desc', 'image', 'category', 'p_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """
        Добавляет Bootstrap-классы к виджетам полей формы.
        """

        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ in ['Select', 'SelectMultiple']:
                field.widget.attrs.update({'class': 'form-select'})
            elif field.widget.__class__.__name__ in ['ClearableFileInput', 'FileInput']:
                field.widget.attrs.update({'class': 'form-control-file'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        """
            Реализует проверку на одинаковые слова в поле 'name_product' и 'desc' а так же на запрещенные слова в случае
            положительного результата вызывает ошибку.
         """

        cleaned_data = super().clean()
        name_product = cleaned_data.get('name_product')
        desc = cleaned_data.get('desc')

        if name_product and desc and name_product == desc:
            self.add_error('name_product', 'Продукты и категории продуктов не могут быть одинаковыми' )

        for word in words:
            if word.lower() in name_product.lower():
                self.add_error("name_product", f"Название не может содержать запрещённое слово: «{word}»")
            if word.lower() in desc.lower():
                self.add_error("desc", f"Описание не может содержать запрещённое слово: «{word}»")

        return cleaned_data

    def clean_p_price(self):
        """
            Реализует проверку на отрицательные цены товаров в случае отрицательной цены вызывает ошибку.
        """
        price = self.cleaned_data.get("p_price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной")
        return price



class ProductModeratorForm(forms.ModelForm):
    """
        Форма для модератора позволяющая включать и выключать публикацию товара.
    """
    class Meta:
        model = Product
        fields = ['publication_sign']