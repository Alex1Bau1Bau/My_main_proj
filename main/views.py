from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Articles
from .forms import ArticlesForm, RegisterUserForm, LoginUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

def index(request):
    return render(request, "main/index.html")

def jsProj(request):
    return render(request, "main/js_proj.html")

class RegisterUser(CreateView):
    # в формс создаем стили
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = '/main/'

    # при регистрации сразу вход в аккаунт
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Reg")
    #     return dict(list(context.items()) + list(c_def.items()))

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')