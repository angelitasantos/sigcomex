from django.db import models


class Teste1Categoria(models.Model):
    STATUS_CHOICES = [
        ('A', 'ATIVO'),
        ('I', 'INATIVO'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome


class Teste1Grupo(models.Model):
    STATUS_CHOICES = [
        ('A', 'ATIVO'),
        ('I', 'INATIVO'),
    ]
    nome = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.nome


class Teste1Cliente(models.Model):
    STATUS_CHOICES = [
        ('A', 'ATIVO'),
        ('I', 'INATIVO'),
    ]

    nome = models.CharField(
        max_length=50, verbose_name='NOME FANTASIA', null=True, blank=True)
    razao_social = models.CharField(
        max_length=200, verbose_name='RAZÃO SOCIAL', null=True, blank=True)
    cnpj = models.CharField(
        max_length=25, verbose_name='CNPJ', null=True, blank=True)
    insc_est = models.CharField(
        max_length=25, verbose_name='INSC EST', null=True, blank=True)
    sigla_imp = models.CharField(
        max_length=5, verbose_name='SIGLA IMP', null=True, blank=True)
    sigla_exp = models.CharField(
        max_length=5, verbose_name='SIGLA EXP', null=True, blank=True)
    serv_sigla_imp = models.CharField(
        max_length=5, verbose_name='SIGLA IMP SERV', null=True, blank=True)
    serv_sigla_exp = models.CharField(
        max_length=5, verbose_name='SIGLA EXP SERV', null=True, blank=True)
    cod_interno = models.CharField(
        max_length=25, verbose_name='COD INTERNO', null=True, blank=True)
    observacoes = models.TextField(
        verbose_name='OBSERVACOES', null=True, blank=True)

    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES)

    grupo = models.ForeignKey(Teste1Grupo, related_name='grupos',
                              on_delete=models.SET_NULL,
                              null=True, blank=True)

    categoria = models.ForeignKey(Teste1Categoria, related_name='categorias',
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True)

    def __str__(self):
        return self.nome
