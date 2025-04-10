from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from parceiros.models import (Teste1Cliente)
from parceiros.forms import (ClienteForm)
from django.contrib import messages
from django.db.models import Q
import pandas as pd
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger,
                                   )


class HonorarioView(View):
    template_name = 'faturamento/honorarios.html'

    def get(self, request):
        title = 'HONORARIOS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, HonorarioView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class TipoServicoView(View):
    template_name = 'faturamento/tipos_servicos.html'

    def get(self, request):
        title = 'TIPOS SERVIÇOS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, TipoServicoView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class ControleSdaView(View):
    template_name = 'faturamento/controle_sda.html'

    def get(self, request):
        title = 'SDAs'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ControleSdaView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class OutroView(View):
    template_name = 'faturamento/notas_debito.html'

    def get(self, request):
        title = 'OUTROS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, OutroView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class FaturamentoView(View):
    template_name = 'faturamento/faturamento.html'

    def get(self, request):
        title = 'FATURAMENTO'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, FaturamentoView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class NotaFiscalView(View):
    template_name = 'faturamento/notas_fiscais.html'

    def get(self, request):
        title = 'NOTAS FISCAIS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, NotaFiscalView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })
