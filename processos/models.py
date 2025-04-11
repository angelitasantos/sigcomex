from django.db import models
from parceiros.models import (Teste1Cliente)


class Teste1TipoComex(models.Model):
    STATUS_CHOICES = [
        ('A', 'ATIVO'),
        ('I', 'INATIVO'),
    ]
    EMPRESA_GRUPO_CHOICES = [
        ('TD', 'TODAS'),
        ('PC', 'PLENO COMEX'),
        ('PS', 'PLENO SERVICOS'),
        ('LG', 'LOGISTICA'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES)
    empresa_grupo = models.CharField(
        max_length=2, choices=EMPRESA_GRUPO_CHOICES)

    def __str__(self):
        return self.nome


class Teste1ProcessoComex(models.Model):
    choices_status = (('N', 'NÃO INICIADO'),
                      ('E', 'EM ANDAMENTO'),
                      ('A', 'A FATURAR'),
                      ('F', 'FATURADO'),
                      ('V', 'VERIFICAR'),
                      ('C', 'CONCLUIDO'))
    status = models.CharField(
        max_length=2, choices=choices_status, default='N')

    choices_comex = (('I', 'IMPORTAÇÃO'),
                     ('E', 'EXPORTAÇÃO'),
                     ('O', 'OUTRO'))
    comex = models.CharField(
        max_length=2, choices=choices_comex, default='I')

    choices_modal = (('M', 'MARITIMO'),
                     ('A', 'AEREO'),
                     ('R', 'RODOVIARIO'),
                     ('C', 'COURIER'),
                     ('P', 'POSTAL'),
                     ('O', 'OUTRO'))
    modal = models.CharField(
        max_length=2, choices=choices_modal, default='M')

    data_abertura = models.DateTimeField(
        auto_now_add=True, verbose_name='Data Abertura', null=True, blank=True)
    codigo_processo = models.CharField(
        max_length=20, verbose_name='Codigo Processo', null=True, blank=True)
    ref_cliente = models.CharField(
        max_length=50, verbose_name='Ref Cliente', null=True, blank=True)
    numero_alternativo = models.CharField(
        max_length=10, verbose_name='Num Alternativo', null=True, blank=True)
    observacoes = models.TextField(
        verbose_name='OBSERVACOES', null=True, blank=True)

    empresa_id = models.CharField(
        max_length=10, verbose_name='Empresa', null=True, blank=True)
    cliente = models.ForeignKey(Teste1Cliente, null=True, blank=True,
                                on_delete=models.SET_NULL)
    empresa_tipo = models.ForeignKey(Teste1TipoComex, null=True, blank=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.data_abertura} - {self.codigo_processo}'

    class Meta:
        ordering = ('-id',)
