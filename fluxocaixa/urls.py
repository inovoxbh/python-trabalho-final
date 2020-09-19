from django.urls import path
from .views import vindex, vtitulopagar

urlpatterns = [
    path('', vindex.index, name='index'),
    path('pagar/titulos/', vtitulopagar.titulos, name='titulospagar'),
    path('pagar/<int:tituloid>', vtitulopagar.titulo, name='titulopagar'),
    path('pagar/novo/', vtitulopagar.novo, name='novo_titulopagar'),
    path('pagar/deletar/<int:tituloid>', vtitulopagar.deletar, name='deletar_titulopagar'),
]