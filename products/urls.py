from django.urls import path, include
from products import views


app_name = "products"

urlpatterns = [
    path("read/<int:pk>/", views.read, name="read"),
    path("create/", views.create, name="create"),
    path("update/<int:pk>/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
    path("update_cnt/", views.update_cnt, name="update_cnt"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path('<int:pk>/comments/delete/', views.delete_comment, name='delete_comment'),
]
