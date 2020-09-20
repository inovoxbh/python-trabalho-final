from django.urls import path
from .views import vindex, vtitulopagar, vtituloreceber, vformapgto, vclassificacaopagar, vclassificacaoreceber, vrelatorios, vfluxo, vsaldoinicial

urlpatterns = [
    path('', vindex.index, name='index'),
    
    path('relatorios/pagar', vrelatorios.pagar, name='relatorio_pagar'),
    path('relatorios/receber', vrelatorios.receber, name='relatorio_receber'),

    path('relatoriofluxo/previsto', vfluxo.previsto, name='fluxo_previsto'),
    path('relatoriofluxo/realizado', vfluxo.realizado, name='fluxo_realizado'),

    path('saldoinicial/saldoinicial/', vsaldoinicial.saldoinicial, name='saldoinicial'),
    path('saldoinicial/novo/', vsaldoinicial.novo, name='novo_saldoinicial'),
    path('saldoinicial/deletar/<int:saldoinicialid>', vsaldoinicial.deletar, name='deletar_saldoinicial'),
    path('saldoinicial/atualizar/<int:saldoinicialid>', vsaldoinicial.atualizar, name='atualizar_saldoinicial'),

    path('pagar/titulos/', vtitulopagar.titulos, name='titulospagar'),
    path('pagar/<int:tituloid>', vtitulopagar.titulo, name='titulopagar'),
    path('pagar/novo/', vtitulopagar.novo, name='novo_titulopagar'),
    path('pagar/deletar/<int:tituloid>', vtitulopagar.deletar, name='deletar_titulopagar'),
    path('pagar/atualizar/<int:tituloid>', vtitulopagar.atualizar, name='atualizar_titulopagar'),

    path('receber/titulos/', vtituloreceber.titulos, name='titulosreceber'),
    path('receber/<int:tituloid>', vtituloreceber.titulo, name='tituloreceber'),
    path('receber/novo/', vtituloreceber.novo, name='novo_tituloreceber'),
    path('receber/deletar/<int:tituloid>', vtituloreceber.deletar, name='deletar_tituloreceber'),
    path('receber/atualizar/<int:tituloid>', vtituloreceber.atualizar, name='atualizar_tituloreceber'),

    path('formapgto/formaspgto/', vformapgto.formaspgto, name='formaspgto'),
    path('formapgto/<int:formapgtoid>', vformapgto.formapgto, name='formapgto'),
    path('formapgto/nova/', vformapgto.nova, name='nova_formapgto'),
    path('formapgto/deletar/<int:formapgtoid>', vformapgto.deletar, name='deletar_formapgto'),
    path('formapgto/atualizar/<int:formapgtoid>', vformapgto.atualizar, name='atualizar_formapgto'),

    path('classificacaopagar/classificacoespagar/', vclassificacaopagar.classificacoespagar, name='classificacoespagar'),
    path('classificacaopagar/<int:classificacaoid>', vclassificacaopagar.classificacaopagar, name='classificacaopagar'),
    path('classificacaopagar/nova/', vclassificacaopagar.nova, name='nova_classificacaopagar'),
    path('classificacaopagar/deletar/<int:classificacaoid>', vclassificacaopagar.deletar, name='deletar_classificacaopagar'),
    path('classificacaopagar/atualizar/<int:classificacaoid>', vclassificacaopagar.atualizar, name='atualizar_classificacaopagar'),

    path('classificacaoreceber/classificacoesreceber/', vclassificacaoreceber.classificacoesreceber, name='classificacoesreceber'),
    path('classificacaoreceber/<int:classificacaoid>', vclassificacaoreceber.classificacaoreceber, name='classificacaoreceber'),
    path('classificacaoreceber/nova/', vclassificacaoreceber.nova, name='nova_classificacaoreceber'),
    path('classificacaoreceber/deletar/<int:classificacaoid>', vclassificacaoreceber.deletar, name='deletar_classificacaoreceber'),
    path('classificacaoreceber/atualizar/<int:classificacaoid>', vclassificacaoreceber.atualizar, name='atualizar_classificacaoreceber'),
]