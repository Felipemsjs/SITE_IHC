"""projeto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('404/', views.error_404_view, name='error_404'),
    path('500/', views.error_500_view, name='error_500'),
    path('blank/', views.blank_view, name='blank'),
    path('buttons/', views.buttons_view, name='buttons'),
    path('cards/', views.cards_view, name='cards'),
    path('charts/', views.charts_view, name='charts'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('index/', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  # Alterado para apontar para a função correta
    path('tables/', views.tables_view, name='tables'),
    path('utilities-animation/', views.utilities_animation_view, name='utilities_animation'),
    path('utilities-border/', views.utilities_border_view, name='utilities_border'),
    path('utilities-color/', views.utilities_color_view, name='utilities_color'),
    path('utilities-other/', views.utilities_other_view, name='utilities_other'),
    path('logout/', views.logout_view, name='logout'),
]
