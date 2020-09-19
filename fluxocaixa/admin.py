from django.contrib import admin
from .models import TituloPagar,ClassificacaoPagar,FormaPagamento

admin.site.register(TituloPagar)
admin.site.register(ClassificacaoPagar)
admin.site.register(FormaPagamento)