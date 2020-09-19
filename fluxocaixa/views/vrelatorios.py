from django.http import HttpResponse
from fluxocaixa.models import TituloPagar, TituloReceber
from django.template import loader
from django.shortcuts import render, redirect

def filtro(request):
    return render(request, 'relatorios/filtro.html')

def pagar(request):
    db_lista = TituloPagar.objects.all().order_by('data_vencimento')
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('relatorios/pagar.html')
    return HttpResponse(template.render(payload, request))

def receber(request):
    db_lista = TituloReceber.objects.all().order_by('data_expectativa')
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('relatorios/receber.html')
    return HttpResponse(template.render(payload, request))
