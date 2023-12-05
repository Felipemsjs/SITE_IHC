from django.contrib import admin
from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.models import User

# Se você tiver um modelo de usuário personalizado
# admin.site.register(CustomUser)


admin.site.register(CustomUser)
