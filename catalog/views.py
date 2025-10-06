from symtable import Class

from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductListView(ListView):
    model = Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    return render(request, template_name='catalog/contacts.html')



class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'



    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)





class ProductEditView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        if product.owner != request.user and not request.user.is_superuser:
            raise PermissionDenied("Вы не владелец этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        user = self.request.user
        if user.is_superuser:
            return ProductForm
        if user .has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.delete_product"

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()


        if product.owner == request.user or request.user.has_perm(
                "catalog.can_delete_product") or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("У вас нет прав.")


