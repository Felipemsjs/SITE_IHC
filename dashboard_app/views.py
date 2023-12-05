from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_view(request):
    print("A view de login foi chamada")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            print("return index")
            return redirect('index')
        else:
            messages.error(request, 'Email ou senha inválidos')

    return render(request, 'login.html')


def home(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Houve um erro no formulário.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def error_404_view(request):
    return render(request, '404.html')

def error_500_view(request):
    return render(request, '500.html')

def blank_view(request):
    return render(request, 'blank.html')

def buttons_view(request):
    return render(request, 'buttons.html')

def cards_view(request):
    return render(request, 'cards.html')

def charts_view(request):
    return render(request, 'charts.html')

def forgot_password_view(request):
    return render(request, 'forgot-password.html')

@login_required
def index_view(request):
    return render(request, 'index.html')

def register_view(request):
    return render(request, 'register.html')

def tables_view(request):
    return render(request, 'tables.html')

def utilities_animation_view(request):
    return render(request, 'utilities-animation.html')

def utilities_border_view(request):
    return render(request, 'utilities-border.html')

def utilities_color_view(request):
    return render(request, 'utilities-color.html')

def utilities_other_view(request):
    return render(request, 'utilities-other.html')

