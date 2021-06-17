from django.urls import path

from . import views
from .views import function

urlpatterns = [
    path('home/',views.function, name="home"),
    path('about/', views.fun2),
    path('create/', views.createPost, name="create"),
    path('update/<str:_id>', views.updatePost, name="update"),
    path('mypost/<str:_id>', views.myPost, name="mypost"),
    path('delete/<str:_id>', views.createPost, name="delete"),

]
