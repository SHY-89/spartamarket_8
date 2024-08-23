from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.views.decorators.http import require_http_methods,require_POST



def index(request):
    index = Product.objects.all()
    context = {
        "index" : index,
    }
    return render(request, "products/index.html", context)


@ require_http_methods(["GET", "POST"])
def create(request):
    if not request.user.is_authenticated:
        return redirect("accounts:login")
    if request.method == 'POST':
        forms = ProductForm(request.POST, request.FILES)
        if forms.is_valid():
            products = forms.save(commit=False)
            products.uuid = request.user
            products.save()
            return redirect("products:read", products.pk)
        
    else:
        forms = ProductForm()
        
    context = { "forms" : forms
        }
    return render(request, "products/create.html", context)


def read(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {
        'product': product
    }
    return render(request, "products/read.html", context)


@ require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Product,pk=pk)
    if product.uuid.pk != request.user.pk:
        return redirect("index")
    if request.method == 'POST':
            forms = ProductForm(request.POST, request.FILES, instance=product)
            if forms.is_valid():
                forms.save()
            return redirect("products:read", pk)
    else:
        forms = ProductForm(instance=product)
    context = {
        
        'forms':forms
    }
    
    return render(request, "products/update.html", context)


@ require_POST
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.uuid.pk == request.user.pk:
        product.delete()
    return redirect("index")

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:read", pk)
    return redirect("accounts:login")