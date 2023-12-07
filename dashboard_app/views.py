from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, login
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Projeto, Dados, CustomUser
import datetime
from .forms import DepartamentoForm

def departamento_create_view(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_departamento')  # Redirecionar para onde você quiser após o cadastro
    else:
        form = DepartamentoForm()
    return render(request, 'departamento.html', {'form': form})

@csrf_exempt  # Idealmente, utilize um mecanismo de proteção CSRF apropriado
@login_required  # Garante que o usuário esteja autenticado
def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        # Criando um novo projeto
        projeto = Projeto.objects.create(
            nome='Projeto ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            descricao='Projeto criado a partir do upload CSV em ' + datetime.datetime.now().strftime("%Y-%m-%d"),
        )

        # Associar o usuário autenticado ao projeto
        if request.user.is_authenticated:
            projeto.usuarios.add(request.user)

        # Processando as linhas do CSV e criando objetos Dados
        for row in reader:
            Dados.objects.create(
                projeto=projeto,
                date=row['Date'] if row['Date'] else '',
                time=row['Time'] if row['Time'] else '',
                time_seconds=row['Time Seconds'] if row['Time Seconds'] else '',
                billable=row['Billable'] if row['Billable'] else '',
                member=row['Member'] if row['Member'] else '',
                board=row['Board'] if row['Board'] else '',
                card=row['Card'] if row['Card'] else '',
                card_labels=row['Card labels'] if row['Card labels'] else '',
                estimate=row['Estimate'] if row['Estimate'] else '',
                estimate_seconds=row['Estimate Seconds'] if row['Estimate Seconds'] else '',
                list=row['List'] if row['List'] else '',
                comment=row['Comment'] if row['Comment'] else '',
                billable_time=row['Billable time'] if row['Billable time'] else '',
                billable_amount=row['Billable amount'] if row['Billable amount'] else '',
                non_billable_time=row['Non-billable time'] if row['Non-billable time'] else '',
            )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'invalid request'}, status=400)

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

def departamento_view(request):
    return render(request, 'departamento.html')

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

