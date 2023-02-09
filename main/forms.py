from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name article'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons article'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date article'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'text article'
            }),
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # стили не изменились дублируем другие
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            # 'username', 'password1', 'password2' - значения берем через админ панель _ пользователи _ в полях имени и пароля _ прав кн мыши _ посмотреть код
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Loginn', widget=forms.TextInput(attrs={'class': 'form-input'})),
    password = forms.CharField(label='Passwordd', widget=forms.PasswordInput(attrs={'class': 'form-input'})),