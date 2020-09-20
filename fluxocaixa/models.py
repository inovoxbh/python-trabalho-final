from django.db import models

class ClassificacaoManager(models.Manager):
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

    objects = ClassificacaoManager()        

class ClassificacaoReceber(models.Model):
    descricao = models.CharField(max_length=30)

    def __str__ (self):
        return self.descricao

    objects = ClassificacaoManager()        

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

class TituloManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def titulo(self,tituloid):
        result = self.filter(id=tituloid)
        return result

class TituloPagar(models.Model):
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(
        blank=True,
        null=True
    )
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.CharField(max_length=100)
    classificacao = models.ForeignKey(
        ClassificacaoPagar,
        on_delete=models.RESTRICT,
        null=True)
    formapagamento = models.ForeignKey(
        FormaPagamento,
        on_delete=models.RESTRICT,
        null=True)
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

    objects = TituloManager()

class TituloReceber(models.Model):
    data_expectativa = models.DateField()
    data_recebimento = models.DateField(
        blank=True,
        null=True
    )
    valor = models.DecimalField(max_digits=11, decimal_places=2)
    descricao = models.CharField(max_length=100)
    classificacao = models.ForeignKey(
        ClassificacaoReceber,
        on_delete=models.RESTRICT,
        null=True)
    formapagamento = models.ForeignKey(
        FormaPagamento,
        on_delete=models.RESTRICT,
        null=True)
    OPCOES_SITUACAO = [
        ('RC','Recebido'),
        ('AR','A Receber')
    ]
    situacao = models.CharField(
        max_length=2,
        choices=OPCOES_SITUACAO,
        default='AR'
    )

    def __str__ (self):
        return f"{self.descricao}, R$ {self.valor}, vencimento em {self.data_expectativa}."

    objects = TituloManager()

class SaldoInicialManager(models.Manager):
    def todos(self):
        result = self.all()
        return result

    def saldoinicial(self,saldoinicialid):
        result = self.filter(id=saldoinicialid)
        return result

class SaldoInicial(models.Model):
    valorinicial = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__ (self):
        return self.valorinicial

    objects = SaldoInicialManager()