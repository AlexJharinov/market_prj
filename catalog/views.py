from symtable import Class

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.forms import ProductForm
from catalog.models import Product

class ProductListView(ListView):
    model = Product


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    return render(request, template_name='contacts.html')



class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ("name_product", "desc", "image", "category", "p_price")
    success_url = reverse_lazy('catalog:product_list')


# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('catalog:base')
#     else:
#         form = ProductForm()
#     return render(request, 'product_form.html', {'form': form})