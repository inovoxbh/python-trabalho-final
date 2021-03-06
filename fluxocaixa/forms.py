from django.forms import ModelForm
from .models import TituloPagar, TituloReceber, FormaPagamento, ClassificacaoPagar, ClassificacaoReceber, SaldoInicial

class TituloPagarForm(ModelForm):
    class Meta:
        model = TituloPagar
        fields = ['data_vencimento','data_pagamento','valor','descricao','classificacao','formapagamento','situacao']

class TituloReceberForm(ModelForm):
    class Meta:
        model = TituloReceber
        fields = ['data_expectativa','data_recebimento','valor','descricao','classificacao','formapagamento','situacao']

class FormaPagamentoForm(ModelForm):
    class Meta:
        model = FormaPagamento
        fields = ['descricao']

class ClassificacaoPagarForm(ModelForm):
    class Meta:
        model = ClassificacaoPagar
        fields = ['descricao']

class ClassificacaoReceberForm(ModelForm):
    class Meta:
        model = ClassificacaoReceber
        fields = ['descricao']

class SaldoInicialForm(ModelForm):
    class Meta:
        model = SaldoInicial
        fields = ['valorinicial']                