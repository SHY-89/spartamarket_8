from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Index
from django.views.decorators.http import require_http_methods,require_POST



def index(request):
    index = Index.objects.all()
    context = {
        "index" : index,
    }
    return render(request, "index.html", context)


def products(request):
    return render(request, "product.html")


@ require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("index")
        
    else:
        forms = ProductForm()
        
    context = { "forms" : forms
        }
    return render(request, "create.html", context)


def read(request, pk):
    product = get_object_or_404(Index,pk=pk)
    context = {
        
        'product': product
    }
    return render(request, "read.html", context)


@ require_http_methods(["GET", "POST"])
def update(request, pk):
    product = get_object_or_404(Index,pk=pk)
    if request.method == 'POST':
        forms = ProductForm(request.POST, instance=product)
        if forms.is_valid():
            forms.save()
            return redirect("index")
        
    else:
        forms = ProductForm(instance=product)
    context = {
        
        'forms':forms
    }
    
    return render(request, "update.html", context)


@ require_POST
def delete(request, pk):
    product = get_object_or_404(Index, pk=pk)
    product.delete()
    return redirect("index")



    # like_user = models.Foreingkey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name="like_products",
    #     null=True 
    # )

@require_POST
def like(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Index, pk=pk)
        if product.like_users.filter(pk=request.user.pk).exists():
            product.like_users.remove(request.user)
        else:
            product.like_users.add(request.user)
        return redirect("products:read", pk)
    return redirect("accounts:login")