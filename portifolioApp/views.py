from django.shortcuts import render
from .models import Projeto


def index(request):
    return render(request,'index.html')

def projetos(request):

    data = {}
    data['projetos'] = Projeto.objects.all()

    return render(request,'projetos.html',data)

def contato(request):
    return render(request,'contato.html')