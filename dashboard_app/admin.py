from django.contrib import admin
from .models import CustomUser, Departamento, Projeto, Dados
from django.contrib import admin
from django.contrib.auth.models import User

# Se você tiver um modelo de usuário personalizado
# admin.site.register(CustomUser)


admin.site.register(CustomUser)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'departamento')
    search_fields = ('nome', 'descricao', 'departamento__nome')
    filter_horizontal = ('usuarios',)


class DadosAdmin(admin.ModelAdmin):
    list_display = ['projeto', 'date', 'member', 'card', 'billable']
    list_filter = ['projeto', 'billable']
    search_fields = ['card', 'member']

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Dados, DadosAdmin)

