from django.http import HttpResponse
from fluxocaixa.models import SaldoInicial
from fluxocaixa.forms import SaldoInicialForm
from django.template import loader
from django.shortcuts import render, redirect

def saldoinicial(request):
    db_lista = SaldoInicial.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('saldoinicial/listar.html')
    return HttpResponse(template.render(payload, request))

def novo(request):
    data = {}
    form = SaldoInicialForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('saldoinicial')
    
    data['form'] = form
    return render(request, 'saldoinicial/form.html', data)

def deletar(request,saldoinicialid):
    db_entidade = SaldoInicial.objects.saldoinicial(saldoinicialid=saldoinicialid)
    db_entidade.delete()

    return redirect('saldoinicial')

def atualizar(request,saldoinicialid):
    data = {}
    db_entidade = SaldoInicial.objects.get(id=saldoinicialid)
    
    form = SaldoInicialForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('saldoinicial')

    data['form'] = form
    return render(request, 'saldoinicial/form.html', data)