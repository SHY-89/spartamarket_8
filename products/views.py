from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, CommentForm
from .models import Product, Comment
from django.views.decorators.http import require_http_methods,require_POST
from django.db.models import Count, Q
from django.http import JsonResponse



def index(request):
    serch_text = request.GET.get('serch_text') or ''
    orders = request.GET.get('orders') or 'date'
    
    
    if orders == 'date':
        if serch_text:
            index = Product.objects.filter(Q(title__icontains=serch_text)|Q(content__icontains=serch_text)|Q(uuid__username__icontains=serch_text)).order_by("-pk")
        else:
            index = Product.objects.all().order_by('-pk')
    else:
        if serch_text:
            index = Product.objects.filter(Q(title__icontains=serch_text)|Q(content__icontains=serch_text)|Q(uuid__username__icontains=serch_text)).annotate(like_users_count=Count('like_users')).order_by('-like_users_count',"-pk")
        else:
            index = Product.objects.all().annotate(like_users_count=Count('like_users')).order_by('-like_users_count', '-pk')
    
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
    product = get_object_or_404(Product, pk=pk)
    comment_form = CommentForm()
    comments = product.comments.all().order_by('-created_at')
    context = {
        'product': product,
        'comment_form': comment_form,
        'comments': comments,
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


@ require_POST
def update_cnt(request):
    pk = request.POST.get('pk')
    product = get_object_or_404(Product, pk=pk)
    product.cnt += 1
    product.save()
    context = {
        "data": '200',
    }
    return JsonResponse(context)


def comment_create(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        text = request.POST.get('text')
        author = request.user
        comment = Comment.objects.create(product=product, text=text, author=author)
        
        # 댓글 최신순 정렬
        comments = Comment.objects.filter(product=product).order_by('-created_at')
        comments_data = [
            {
                'id': comment.id,
                'text': comment.text,
                'author': comment.author.username,
                'created_at': comment.created_at.isoformat()  # ISO 8601 형식으로
            }
            for comment in comments
        ]
        
        return JsonResponse({'comments': comments_data})
    

@require_POST
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        comment.delete()
    return JsonResponse({'status': 'success'})
