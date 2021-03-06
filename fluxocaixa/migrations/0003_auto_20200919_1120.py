# Generated by Django 3.1 on 2020-09-19 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fluxocaixa', '0002_classificacaoreceber_tituloreceber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='titulopagar',
            name='classificacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fluxocaixa.classificacaopagar'),
        ),
        migrations.AlterField(
            model_name='titulopagar',
            name='data_pagamento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='titulopagar',
            name='formapagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fluxocaixa.formapagamento'),
        ),
        migrations.AlterField(
            model_name='tituloreceber',
            name='classificacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fluxocaixa.classificacaoreceber'),
        ),
        migrations.AlterField(
            model_name='tituloreceber',
            name='data_recebimento',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='tituloreceber',
            name='formapagamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='fluxocaixa.formapagamento'),
        ),
    ]
