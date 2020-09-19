from django.http import HttpResponse
from fluxocaixa.models import TituloReceber
from fluxocaixa.forms import TituloReceberForm
from django.template import loader
from django.shortcuts import render, redirect

def titulos(request):
    db_lista = TituloReceber.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('tituloreceber/listar.html')
    return HttpResponse(template.render(payload, request))

def titulo(request,tituloid):
    db_entidade = TituloReceber.objects.titulo(tituloid=tituloid).values()
    payload = { 'lista' : list(db_entidade) }
    template = loader.get_template('tituloreceber/detalhar.html')
    return HttpResponse(template.render(payload, request))

def novo(request):
    data = {}
    form = TituloReceberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('titulosreceber')
    
    data['form'] = form
    return render(request, 'tituloreceber/form.html', data)

def deletar(request,tituloid):
    db_entidade = TituloReceber.objects.titulo(tituloid=tituloid)
    db_entidade.delete()

    return redirect('titulosreceber')

def atualizar(request,tituloid):
    data = {}
    db_entidade = TituloReceber.objects.get(id=tituloid)
    
    form = TituloReceberForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('titulosreceber')

    data['form'] = form
    return render(request, 'tituloreceber/form.html', data)