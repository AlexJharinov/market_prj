
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.services import get_product_from_cache, get_products_by_category_id


class ProductListView(ListView):
    """
        Отображает список всех объектов модели Product.
    """
    model = Product

    def get_queryset(self):
        return get_product_from_cache()

def contacts(request):
    """
        Обрабатывает страницу контактов и принимает сообщения от пользователей и дает обратную связь.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    return render(request, template_name='catalog/contacts.html')



class ProductDetailView(DetailView):
        """
            Класс для отображения деталей одного продукта
        """

        model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
        Класс для создания продукта.
    """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductEditView(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования продукта.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        """
            Проверяет права доступа на владельца и суперюзера в случае отсутствия прав вызывает ошибку
        """
        product = self.get_object()
        if product.owner != request.user and not request.user.is_superuser:
            raise PermissionDenied("Вы не владелец этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        """
            Проверка на пользователя и возвращения формы в зависимости от прав пользователя
        """
        user = self.request.user
        if user.is_superuser:
            return ProductForm
        if user .has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    """
        Класс для удаления продукта.
    """
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.delete_product"

    def dispatch(self, request, *args, **kwargs):
        """
            Проверяет права пользователя и в зависимости от прав дает разрешение или вызывает ошибку.
        """
        product = self.get_object()

        if product.owner == request.user or request.user.has_perm(
                "catalog.can_delete_product") or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("У вас нет прав.")

from catalog.models import Product, Category


class ProductsByCategoryView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"
    paginate_by = 12

    def get_queryset(self):
        self.category_id = int(self.kwargs.get("pk"))
        self.category, qs = get_products_by_category_id(self.category_id, published_only=True)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["categories"] = Category.objects.all().order_by("name_category")
        return ctx


class CategoryChooserView(TemplateView):
    template_name = "catalog/category_choose.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.all().order_by("name_category")
        return ctx

    def post(self, request, *args, **kwargs):
        category_id = request.POST.get("category_id")
        if category_id:
            return redirect("catalog:products_by_category", pk=category_id)
        return self.get(request, *args, **kwargs)



