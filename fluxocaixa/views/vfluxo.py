from django.http import HttpResponse
from fluxocaixa.models import TituloPagar, TituloReceber
from django.template import loader
from django.shortcuts import render, redirect

def previsto(request):
    db_lista_pagar = TituloPagar.objects.filter(situacao="AP").order_by('data_vencimento','classificacao')
    db_lista_receber = TituloReceber.objects.filter(situacao="AR").order_by('data_expectativa','classificacao')

    dados ="<h1>Títulos Previstos a Pagar</h1>"
    dados += "<br />"
    dados += "<ul>"
    for i in db_lista_pagar:
        titulo = TituloPagar.objects.get(id=i.id)
        
        ano =titulo.data_vencimento.year
        mes =titulo.data_vencimento.month
        dados += "<li>" + str(ano) + ',' + str(mes) + "</li>"
    dados += "</ul>"

    return HttpResponse(dados)

#    payload = {
#        'lista_pagar' : list(db_lista_pagar),
#        'lista_receber' : list(db_lista_receber),
#    }
#    template = loader.get_template('fluxo/previsto.html')
#    return HttpResponse(template.render(payload, request))

def realizado(request):
    db_lista_pagar = TituloPagar.objects.filter(situacao="PG").order_by('data_vencimento','classificacao')
    db_lista_receber = TituloReceber.objects.filter(situacao="RC").order_by('data_expectativa','classificacao')
    
    payload = {
        'lista_pagar' : list(db_lista_pagar),
        'lista_receber' : list(db_lista_receber),
    }
    
    template = loader.get_template('fluxo/previsto.html')
    return HttpResponse(template.render(payload, request))