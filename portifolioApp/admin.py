from django.contrib import admin
from .models import Categoria, Projeto, Contato

admin.site.register(Contato)
admin.site.register(Categoria)
admin.site.register(Projeto)