from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.crypto import get_random_string  # Importação necessária para gerar o username aleatório
import uuid

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)  # O email é usado como username
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        self.username = self.email  # Garantir que o username sempre seja o email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuarios = models.ManyToManyField(CustomUser)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome


class Dados(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)  # Mudança para CharField
    time = models.CharField(max_length=20)
    time_seconds = models.CharField(max_length=20)
    billable = models.CharField(max_length=20)
    member = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    card = models.CharField(max_length=100)
    card_labels = models.CharField(max_length=200)
    estimate = models.CharField(max_length=20)
    estimate_seconds = models.CharField(max_length=10)
    list = models.CharField(max_length=100)
    comment = models.TextField(blank=True)
    billable_time = models.CharField(max_length=20)
    billable_amount = models.CharField(max_length=20)
    non_billable_time = models.CharField(max_length=20)



