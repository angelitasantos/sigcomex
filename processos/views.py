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


class ProcessosTemplateView(TemplateView):
    template_name = 'processos/processos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PROCESSOS'
        return context


class ProcessoComexView(View):
    template_name = 'processos/processos_comex.html'

    def get(self, request):
        title = 'PROCESSOS COMEX'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ProcessoComexView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class ProcessoServicoView(View):
    template_name = 'processos/processos_servicos.html'

    def get(self, request):
        title = 'PROCESSOS SERVIÇOS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ProcessoServicoView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class ProcessoNextBHView(View):
    template_name = 'processos/processos_next_bh.html'

    def get(self, request):
        title = 'PROCESSOS NEXT BH'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ProcessoNextBHView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class ProcessoNextSPView(View):
    template_name = 'processos/processos_next_sp.html'

    def get(self, request):
        title = 'PROCESSOS NEXT SP'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ProcessoNextSPView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class ProcessoLeanView(View):
    template_name = 'processos/processos_lean.html'

    def get(self, request):
        title = 'PROCESSOS LEAN'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, ProcessoLeanView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })
