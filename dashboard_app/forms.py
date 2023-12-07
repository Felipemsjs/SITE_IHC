from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome', 'descricao']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')  # Adicione outros campos conforme necessário

    def clean_email(self):
        email = self.cleaned_data['email']
        # Adicione sua lógica de validação para email aqui
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
