from django.urls import path
from .views import user_register, LoginUser, home_view, user_logout
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', home_view, name='home'),
    path('register/', user_register, name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),

]

