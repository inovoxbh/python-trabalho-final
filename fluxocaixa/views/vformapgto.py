from django.http import HttpResponse
from fluxocaixa.models import FormaPagamento
from fluxocaixa.forms import FormaPagamentoForm
from django.template import loader
from django.shortcuts import render, redirect

def formaspgto(request):
    db_lista = FormaPagamento.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('formapagamento/listar.html')
    return HttpResponse(template.render(payload, request))

def formapgto(request,formapgtoid):
    db_entidade = FormaPagamento.objects.formapgto(formapgtoid=formapgtoid).values()
    payload = { 'lista' : list(db_entidade) }
    template = loader.get_template('formapagamento/detalhar.html')
    return HttpResponse(template.render(payload, request))

def nova(request):
    data = {}
    form = FormaPagamentoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('formaspgto')
    
    data['form'] = form
    return render(request, 'formapagamento/form.html', data)

def deletar(request,formapgtoid):
    db_entidade = FormaPagamento.objects.formapgto(formapgtoid=formapgtoid)
    db_entidade.delete()

    return redirect('formaspgto')

def atualizar(request,formapgtoid):
    data = {}
    db_entidade = FormaPagamento.objects.get(id=formapgtoid)
    
    form = FormaPagamentoForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('formaspgto')

    data['form'] = form
    return render(request, 'formapagamento/form.html', data)