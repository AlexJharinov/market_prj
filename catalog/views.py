from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.context_processors import request

from catalog.forms import ProductForm
from catalog.models import Product


# Create your views here.
def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, template_name='detail_inf.html', context=context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    return render(request, template_name='contacts.html')


def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {"product": product}
    return render(request, template_name='product_detail.html', context=context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:base')
    else:
        form = ProductForm()
    return render(request, 'create.html', {'form': form})