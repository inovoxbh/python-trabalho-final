from django.http import HttpResponse
from django.http import JsonResponse
from fluxocaixa.models import TituloPagar
from fluxocaixa.forms import TituloPagarForm
from django.views.decorators.csrf import csrf_exempt
from django.http.multipartparser import MultiPartParser
from django.template import loader
from django.shortcuts import render, redirect

def titulos(request):
    db_lista = TituloPagar.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('titulopagar/listar.html')
    return HttpResponse(template.render(payload, request))

def titulo(request,tituloid):
    db_entidade = TituloPagar.objects.titulo(tituloid=tituloid).values()
    payload = { 'lista' : list(db_entidade) }
    template = loader.get_template('titulopagar/detalhar.html')
    return HttpResponse(template.render(payload, request))

def novo(request):
    data = {}
    form = TituloPagarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('titulospagar')
    
    data['form'] = form
    return render(request, 'titulopagar/form.html', data)

def deletar(request,tituloid):
    db_entidade = TituloPagar.objects.titulo(tituloid=tituloid)
    db_entidade.delete()

    return redirect('titulospagar')

def atualizar(request,tituloid):
    data = {}
    #db_entidade = TituloPagar.objects.titulo(tituloid=tituloid)
    db_entidade = TituloPagar.objects.get(id=tituloid)
    
    form = TituloPagarForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('titulospagar')

    data['form'] = form
    return render(request, 'titulopagar/form.html', data)