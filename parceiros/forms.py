from django import forms
from .models import (Teste1Cliente, Teste1Categoria, Teste1Grupo)


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Teste1Categoria
        fields = [
            'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control form-control-sm', 'autocomplete': 'off'})


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Teste1Grupo
        fields = [
            'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control form-control-sm', 'autocomplete': 'off'})


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Teste1Cliente
        fields = [
            'nome', 'razao_social', 'cnpj', 'insc_est', 'sigla_imp',
            'sigla_exp', 'serv_sigla_imp', 'serv_sigla_exp',
            'cod_interno', 'status', 'grupo', 'categoria', 'observacoes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control form-control-sm',
                 'autocomplete': 'off'})

    nome = forms.CharField(required=True)
    razao_social = forms.CharField(required=True)
    cnpj = forms.CharField(required=False)
    insc_est = forms.CharField(required=False)
    sigla_imp = forms.CharField(required=False)
    sigla_exp = forms.CharField(required=False)
    serv_sigla_imp = forms.CharField(required=False)
    serv_sigla_exp = forms.CharField(required=False)
    cod_interno = forms.CharField(required=False)
    observacoes = forms.CharField(required=False)

    labels = {
            'nome': 'Nome Fantasia',
            'razao_social': 'Razão Social',
            'cnpj': 'CNPJ',
            'insc_est': 'Insc. Est.',
            'sigla_imp': 'Comex IMP.',
            'sigla_exp': 'Comex EXP.',
            'serv_sigla_imp': 'Serv. IMP.',
            'serv_sigla_exp': 'Serv. EXP.',
            'cod_interno': 'Cod Interno',
            'status': 'Status',
            'grupo': 'Grupo',
            'categoria': 'Categoria',
            'observacoes': 'Observacoes',
        }

    grupo_id = forms.ModelChoiceField(
        queryset=Teste1Grupo.objects.all(),
        empty_label="Escolha um Grupo",
        required=False, initial=3,
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}))

    categoria_id = forms.ModelChoiceField(
        queryset=Teste1Categoria.objects.all(),
        empty_label="Escolha uma Categoria",
        required=False, initial=5,
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}))
