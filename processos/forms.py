from django import forms
from .models import (Teste1TipoComex, Teste1ProcessoComex)
from parceiros.models import (Teste1Cliente)


class TipoComexForm(forms.ModelForm):
    class Meta:
        model = Teste1TipoComex
        fields = [
            'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control form-control-sm',
                 'autocomplete': 'off'})


class ProcessosComexForm(forms.ModelForm):
    class Meta:
        model = Teste1ProcessoComex
        fields = [
            'codigo_processo', 'ref_cliente',
            'numero_alternativo', 'status', 'comex', 'modal',
            'empresa_id', 'cliente', 'empresa_tipo', 'observacoes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {'class': 'form-control form-control-sm',
                 'autocomplete': 'off'})

    ref_cliente = forms.CharField(required=True)
    numero_alternativo = forms.CharField(required=False)
    observacoes = forms.CharField(required=False)

    labels = {
            'codigo_processo': 'Cod Proc',
            'ref_cliente': 'Ref.Cliente',
            'numero_alternativo': 'Num. Alt.',
            'empresa_id': 'Empresa',
            'cliente': 'Ciente',
            'empresa_tipo': 'Tipo',
            'status': 'Status',
            'comex': 'Comex',
            'modal': 'Modal',
            'observacoes': 'Observacoes',
        }

    empresa_tipo_id = forms.ModelChoiceField(
        queryset=Teste1TipoComex.objects.all(),
        empty_label="Escolha um Tipo",
        required=False, initial=1,
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}))

    cliente_id = forms.ModelChoiceField(
        queryset=Teste1Cliente.objects.all(),
        empty_label="Escolha o Cliente",
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-control form-control-sm'}))
