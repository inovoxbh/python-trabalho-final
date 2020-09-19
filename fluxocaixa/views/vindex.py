#from django.shortcuts import render
from django.http import HttpResponse
from fluxocaixa.models import TituloPagar

def index(request):
    return HttpResponse("Fluxo de Caixa")