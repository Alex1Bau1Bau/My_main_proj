from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Articles
from .forms import ArticlesForm, RegisterUserForm, LoginUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView

from .parsing import get_data, all_news_dnipro


def index(request):
    return render(request, "main/index.html")

def jsProj(request):
    return render(request, "main/js_proj.html")

def news_parsing_all(request):
    list_news = get_data("https://dniprorada.gov.ua/uk")
    return render(request, "main/all_news_dnipro.html", {"list_news": list_news})

def create_articles(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_articles.html', data)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = '/main/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')

def my_photo(request):
    if request.user.is_authenticated and request.user.username == 'admin':
        return render(request, "main/my_photo.html")
    else:
        return redirect('login')

def my_video(request):
    if request.user.is_authenticated and request.user.username:
        return render(request, "main/my_video.html")
    else:
        return redirect('login')

def my_music(request):
    if request.user.is_authenticated and request.user.username:
        return render(request, "main/my_muzic.html")
    else:
        return redirect('login')