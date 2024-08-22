from django.urls import path, include
from products import views


app_name = "products"

urlpatterns = [
    path("read/<int:pk>/", views.read, name="read"),
    path("create/", views.create, name="create"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),

]
