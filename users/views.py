from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from accounts.forms import UserProfile


def profile(request, username):
    member = get_object_or_404(get_user_model(), username=username)
    products = member.products.all().order_by('-created_at')

    context = {
        "member": member,
        "products": products,
    }
    return render(request, "users/profile.html", context)


@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(get_user_model(), pk=user_id)
        if member != request.user:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("users:profile", username=member.username)
    return redirect("accounts:login")


@require_POST
def update_profile(request):
    if request.user.is_authenticated:
        forms = UserProfile(request.POST, request.FILES, instance=request.user)
        if forms.is_valid():
            forms.save()
        return redirect("users:profile", username=request.user.username)
    return redirect("accounts:login")

def update():
    pass