from django.contrib import admin
from .models import TituloPagar,ClassificacaoPagar,FormaPagamento,ClassificacaoReceber,TituloReceber,SaldoInicial

admin.site.register(TituloPagar)
admin.site.register(ClassificacaoPagar)
admin.site.register(FormaPagamento)
admin.site.register(ClassificacaoReceber)
admin.site.register(TituloReceber)
admin.site.register(SaldoInicial)