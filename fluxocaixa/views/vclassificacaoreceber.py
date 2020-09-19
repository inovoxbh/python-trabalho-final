from django.http import HttpResponse
from fluxocaixa.models import ClassificacaoReceber
from fluxocaixa.forms import ClassificacaoReceberForm
from django.template import loader
from django.shortcuts import render, redirect

def classificacoesreceber(request):
    db_lista = ClassificacaoReceber.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('classificacaoreceber/listar.html')
    return HttpResponse(template.render(payload, request))

def classificacaoreceber(request,classificacaoid):
    db_entidade = ClassificacaoReceber.objects.classificacao(classificacaoid=classificacaoid).values()
    payload = { 'lista' : list(db_entidade) }
    template = loader.get_template('classificacaoreceber/detalhar.html')
    return HttpResponse(template.render(payload, request))

def nova(request):
    data = {}
    form = ClassificacaoReceberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('classificacoesreceber')
    
    data['form'] = form
    return render(request, 'classificacaoreceber/form.html', data)

def deletar(request,classificacaoid):
    db_entidade = ClassificacaoReceber.objects.classificacao(classificacaoid=classificacaoid)
    db_entidade.delete()

    return redirect('classificacoesreceber')

def atualizar(request,classificacaoid):
    data = {}
    db_entidade = ClassificacaoReceber.objects.get(id=classificacaoid)
    
    form = ClassificacaoReceberForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('classificacoesreceber')

    data['form'] = form
    return render(request, 'classificacaoreceber/form.html', data)