from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .form import CustomUserCreationForm
from django.views import generic



class RecipeLoginView(LoginView):
    template_name = 'accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('myapp:recipe_create')

class RecipeLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
    
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')  # 登録成功後にログインページにリダイレクト
    template_name = 'accounts/signup.html'