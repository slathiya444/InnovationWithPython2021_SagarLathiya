from django.urls import path

from . import views
from .views import UserPostListView
from .views import function

urlpatterns = [
    path('',views.function, name="home"),
    path('about/', views.fun2, name="about"),
    path('create/', views.createPost, name="create"),
    path('update/<str:_id>', views.updatePost, name="update"),
    path('mypost/<str:_id>', views.myPost, name="mypost"),
    # path('userpost/<str:_id>', views.userPost, name="userpost"),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('delete/<str:_id>', views.delete, name="delete"),

]
