from django.shortcuts import render, redirect
from .models import Projeto
from .form import ContatoForm

def index(request):
    return render(request,'index.html')

def projetos(request):

    data = {}
    data['projetos'] = Projeto.objects.all()

    return render(request,'projetos.html',data)

def contato(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_contato')
    data = {}
    data['form'] = form
    return render(request,'contato.html',data)