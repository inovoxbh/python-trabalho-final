from django.http import HttpResponse
from fluxocaixa.models import ClassificacaoPagar
from fluxocaixa.forms import ClassificacaoPagarForm
from django.template import loader
from django.shortcuts import render, redirect

def classificacoespagar(request):
    db_lista = ClassificacaoPagar.objects.todos().values()
    payload = { 'lista' : list(db_lista) }
    template = loader.get_template('classificacaopagar/listar.html')
    return HttpResponse(template.render(payload, request))

def classificacaopagar(request,classificacaoid):
    db_entidade = ClassificacaoPagar.objects.classificacao(classificacaoid=classificacaoid).values()
    payload = { 'lista' : list(db_entidade) }
    template = loader.get_template('classificacaopagar/detalhar.html')
    return HttpResponse(template.render(payload, request))

def nova(request):
    data = {}
    form = ClassificacaoPagarForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('classificacoespagar')
    
    data['form'] = form
    return render(request, 'classificacaopagar/form.html', data)

def deletar(request,classificacaoid):
    db_entidade = ClassificacaoPagar.objects.classificacao(classificacaoid=classificacaoid)
    db_entidade.delete()

    return redirect('classificacoespagar')

def atualizar(request,classificacaoid):
    data = {}
    db_entidade = ClassificacaoPagar.objects.get(id=classificacaoid)
    
    form = ClassificacaoPagarForm(request.POST or None, instance=db_entidade)
    if form.is_valid():
        form.save()
        return redirect('classificacoespagar')

    data['form'] = form
    return render(request, 'classificacaopagar/form.html', data)