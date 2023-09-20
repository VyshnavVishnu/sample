from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.Sign,name='Sign'),
    path('register/', views.Register,name='Register'),
    path('login/', views.Login,name='Login'),
    path('gallery/', views.Gallery,name='Gallery'),
    path('home/', views.Home,name='Home'),
    path('view/', views.View,name='View'),
    path('delete_user/<int:id>', views.delete_user,name='delete_user'),
    path('edit/<int:id>', views.edit,name='edit'),
]