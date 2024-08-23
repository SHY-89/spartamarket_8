from django.contrib import admin 
from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
    path("change_password/", views.change_password, name="change_password"),
]
  