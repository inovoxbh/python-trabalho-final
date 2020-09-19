from django.urls import path
from .views import vindex, vtitulopagar, vtituloreceber

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

]