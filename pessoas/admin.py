from django.contrib import admin
from .models import Pessoa

# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'idade']

admin.site.register(Pessoa, PessoaAdmin)