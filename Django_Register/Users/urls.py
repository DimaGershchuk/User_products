from django.urls import path
from .views import user_register, LoginUser, home_view, user_logout, product_list, product_create, product_delete, product_detail, product_update
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', user_register, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/edit/', product_update, name='product_update'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
]

