from django.db import models

class ClassificacaoPagarManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def classificacao(self,classificacaoid):
        result = self.filter(id=classificacaoid)
        return result

class ClassificacaoPagar(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__ (self):
        return self.descricao

    objects = ClassificacaoPagarManager()        

class FormaPagamentoManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def formapgto(self,formapgtoid):
        result = self.filter(id=formapgtoid)
        return result

class FormaPagamento(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__ (self):
        return self.descricao

    objects = FormaPagamentoManager()        

class TituloPagarManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def titulopagar(self,titulopagarid):
        result = self.filter(id=titulopagarid)
        return result

class TituloPagar(models.Model):
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.CharField(max_length=100)
    classificacao = models.ForeignKey(
        ClassificacaoPagar,
        on_delete=models.RESTRICT,
        null="true")
    formapagamento = models.ForeignKey(
        FormaPagamento,
        on_delete=models.RESTRICT,
        null="true")
    OPCOES_SITUACAO = [
        ('PG','Pago'),
        ('AP','A Pagar')
    ]
    situacao = models.CharField(
        max_length=2,
        choices=OPCOES_SITUACAO,
        default='AP'
    )

    def __str__ (self):
        return f"{self.descricao}, R$ {self.valor}, vencimento em {self.data_vencimento}."

    objects = TituloPagarManager()