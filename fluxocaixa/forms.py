from django.forms import ModelForm
from .models import TituloPagar

class TituloPagarForm(ModelForm):
    class Meta:
        model = TituloPagar
        fields = ['data_vencimento','data_pagamento','valor','descricao','classificacao','formapagamento','situacao']