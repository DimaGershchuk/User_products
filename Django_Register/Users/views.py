from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, CustomLoginForm


def home_view(request):
    return render(request, 'home_page.html')


def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')


