from django.http import HttpResponse
from fluxocaixa.models import TituloPagar, TituloReceber, SaldoInicial
from django.template import loader
from django.shortcuts import render, redirect

def nomedomes(mes):
    if (mes == 1):
        nomemes ="Janeiro"
    elif (mes == 2):
        nomemes ="Fevereiro"
    elif (mes == 3):
        nomemes ="Março"
    elif (mes == 4):
        nomemes ="Abril"
    elif (mes == 5):
        nomemes ="Maio"
    elif (mes == 6):
        nomemes ="Junho"
    elif (mes == 7):
        nomemes ="Julho"
    elif (mes == 8):
        nomemes ="Agosto"
    elif (mes == 9):
        nomemes ="Setembro"
    elif (mes == 10):
        nomemes ="Outubro"
    elif (mes == 11):
        nomemes ="Novembro"
    else:
        nomemes ="Dezembro"
    return nomemes


def previsto(request):
    db_lista_pagar = TituloPagar.objects.filter(situacao="AP").order_by('data_vencimento','classificacao')
    db_lista_receber = TituloReceber.objects.filter(situacao="AR").order_by('data_expectativa','classificacao')
    
    # saldo inicial
    db_saldo_inicial = SaldoInicial.objects.all().order_by('id')
    for i in db_saldo_inicial:
        valorinicial =i.valorinicial
    print(valorinicial)
    
    valorreceitastotal =0
    valorreceitasmes =0

    valordespesastotal =0
    valordespesasmes =0

    dados ="<div>"

    if (db_lista_pagar or db_lista_receber):
        anoant =0
        mesant =0

        # despesas
        if (db_lista_pagar):
            dados += "<h1>Despesas Previstas</h1>"
            for i in db_lista_pagar:
                titulo = TituloPagar.objects.get(id=i.id)
                
                ano =titulo.data_vencimento.year
                mes =titulo.data_vencimento.month

                valordespesastotal += titulo.valor

                if ((ano != anoant) or (mes != mesant)):
                    if ((anoant >0) and (mesant >0)):
                        dados += "</table>"

                    dados += "<h2>" + nomedomes(mes) + " de " + str(ano) + "</h2>"
                    dados += "<table border='1'>"
                    dados += "<tr style='background-color: orange'><th>Classificação</th><th>Descrição</th><th>Valor</th><th>Vencimento</th></tr>"
                    anoant =ano
                    mesant =mes
                
                dados += "<tr><td>" + str(titulo.classificacao) + "</td><td>" + str(titulo.descricao) + "</td><td>" + str(titulo.valor) + "</td><td>" + str(titulo.data_vencimento) + "</tr>"
            dados += "</table>"

        # receitas
        if (db_lista_receber):
            dados += "<h1>Receitas Previstas</h1>"
            for i in db_lista_receber:
                titulo = TituloReceber.objects.get(id=i.id)
                
                ano =titulo.data_expectativa.year
                mes =titulo.data_expectativa.month

                valorreceitastotal += titulo.valor

                if ((ano != anoant) or (mes != mesant)):
                    if ((anoant >0) and (mesant >0)):
                        dados += "</table>"

                    dados += "<h2>" + nomedomes(mes) + " de " + str(ano) + "</h2>"
                    dados += "<table border='1'>"
                    dados += "<tr style='background-color: green'><th>Classificação</th><th>Descrição</th><th>Valor</th><th>Expectativa</th></tr>"
                    anoant =ano
                    mesant =mes
                
                dados += "<tr><td>" + str(titulo.classificacao) + "</td><td>" + str(titulo.descricao) + "</td><td>" + str(titulo.valor) + "</td><td>" + str(titulo.data_expectativa) + "</tr>"
            dados += "</table>"

        dados += "<h3>Total despesas: R$ " + str(valordespesastotal) + "</h3>"
        dados += "<h3>Total receitas: R$ " + str(valorreceitastotal) + "</h3>"
    else:
        dados += "<p>Não foram localizados registros para exibição.</p>"

    dados += "</div>"

    return HttpResponse(dados)

def realizado(request):
    db_lista_pagar = TituloPagar.objects.filter(situacao="PG").order_by('data_vencimento','classificacao')
    db_lista_receber = TituloReceber.objects.filter(situacao="RC").order_by('data_expectativa','classificacao')
    
    payload = {
        'lista_pagar' : list(db_lista_pagar),
        'lista_receber' : list(db_lista_receber),
    }
    
    template = loader.get_template('fluxo/previsto.html')
    return HttpResponse(template.render(payload, request))