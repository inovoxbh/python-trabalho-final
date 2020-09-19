from django.urls import path
from .views import vindex, vtitulopagar, vtituloreceber, vformapgto, vclassificacaopagar

urlpatterns = [
    path('', vindex.index, name='index'),

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
]