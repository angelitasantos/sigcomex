from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from parceiros.models import (Teste1Cliente)
from parceiros.forms import (ClienteForm)
from .models import (Teste1TipoComex, Teste1ProcessoComex)
from .forms import (TipoComexForm, ProcessosComexForm)
from django.contrib import messages
from django.contrib.messages import constants
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
    template_name = 'processos/comex/processos_comex.html'

    def get(self, request):
        title = 'PROCESSOS COMEX'
        processos = Teste1ProcessoComex.objects.all().order_by(
            '-id')
        form = ProcessosComexForm()

        tipos_comex = Teste1TipoComex.objects.all()

        query = request.GET.get('q', '')
        status = request.GET.get('status', '')
        comex = request.GET.get('comex', '')
        modal = request.GET.get('modal', '')
        empresa_tipo = request.GET.get('empresa_tipo', '')

        if status:
            processos = processos.filter(status=status)

        if comex:
            processos = processos.filter(comex=comex)

        if modal:
            processos = processos.filter(modal=modal)

        if empresa_tipo:
            processos = processos.filter(empresa_tipo_id=empresa_tipo)

        default_page = 1
        page = request.GET.get('page', default_page)
        processos_per_page = 25

        paginator = Paginator(processos, processos_per_page)
        page_number = request.GET.get('page')
        processos_page = paginator.get_page(page_number)

        try:
            processos_page = paginator.page(page)
        except PageNotAnInteger:
            processos_page = paginator.page(default_page)
        except EmptyPage:
            processos_page = paginator.page(paginator.num_pages)

        return render(request, ProcessoComexView.template_name, {
            'title': title,
            'processos': processos_page,
            'tipos_comex': tipos_comex,
            'query': query,
            'status': status,
            'comex': comex,
            'modal': modal,
            'empresa_tipo': empresa_tipo,
            'form': form
        })

    def post(self, request):
        title = 'PROCESSOS COMEX'
        form = ProcessosComexForm()

        # codigo_processo = request.POST.get('codigo_processo')
        ref_cliente = request.POST.get('ref_cliente')
        # numero_alternativo = request.POST.get('numero_alternativo')
        # observacoes = request.POST.get('observacoes')
        # status = request.POST.get('status')
        comex = request.POST.get('comex')
        modal = request.POST.get('modal')
        # empresa_id = request.POST.get('empresa_id')
        empresa_tipo1 = request.POST.get('empresa_tipo_id')

        empresa_tipo = 1 if empresa_tipo1 is None else empresa_tipo1

        status = 'A'
        if request.method == 'POST' and 'update' in request.POST:
            id = request.POST.get('id_processo')
            # status = request.POST.get('status')
            ref_cliente = request.POST.get('ref_cliente')
            comex = request.POST.get('comex')
            modal = request.POST.get('modal')
            empresa_tipo_id = request.POST.get('empresa_tipo_id')
            processo = get_object_or_404(Teste1ProcessoComex, pk=id)

            # processo.codigo_processo = codigo_processo
            processo.ref_cliente = ref_cliente
            # processo.numero_alternativo = numero_alternativo
            # processo.observacoes = observacoes
            # processo.status = status
            processo.comex = comex
            processo.modal = modal
            # processo.empresa_id = empresa_id
            processo.empresa_tipo_id = empresa_tipo_id
            processo.save()
            msg = f'Processo {processo.codigo_processo} Alterado com Sucesso !'
            messages.success(request, msg)
            return redirect('processos_comex')

        elif request.method == 'POST' and 'search' in request.POST:
            processos = Teste1ProcessoComex.objects.all().order_by(
                '-id')
            tipos_comex = Teste1TipoComex.objects.all()
            query = request.POST.get('query', '')
            status = request.POST.get('status', '')
            comex = request.POST.get('comex', '')
            modal = request.POST.get('modal', '')
            empresa_tipo = request.POST.get('empresa_tipo', '')

            if status:
                processos = processos.filter(status=status)

            if comex:
                processos = processos.filter(comex=comex)

            if modal:
                processos = processos.filter(modal=modal)

            if empresa_tipo:
                processos = processos.filter(empresa_tipo_id=empresa_tipo)

            if query:
                processos = processos.filter(
                    Q(cliente__nome__icontains=query) |
                    Q(cliente__cnpj__icontains=query) |
                    Q(cliente__sigla_imp__icontains=query) |
                    Q(cliente__sigla_exp__icontains=query) |
                    Q(cliente__serv_sigla_imp__icontains=query) |
                    Q(cliente__serv_sigla_exp__icontains=query) |
                    Q(cliente__razao_social__icontains=query)
                    )

            return render(request, ProcessoComexView.template_name, {
                'title': title,
                'processos': processos,
                'status': status,
                'comex': comex,
                'modal': modal,
                'tipos_comex': tipos_comex,
                'form': form
            })

        elif request.method == 'POST' and 'delete' in request.POST:
            id = request.POST.get('id')
            processo = get_object_or_404(Teste1ProcessoComex, pk=id)
            # Teste1ProcessoComex.objects.get(id=id).delete()
            msg = f'Processo {processo.codigo_processo} Excluído com Sucesso !'
            messages.success(request, msg)
            return redirect('processos_comex')


class PComex1View(View):
    template_name = 'processos/comex/comex_gerar_capa.html'

    def get(self, request):
        title = 'COMEX GERAR CAPA'
        processos = Teste1ProcessoComex.objects.all().order_by(
            '-id').filter(status='N')
        form = ProcessosComexForm()

        tipos_comex = Teste1TipoComex.objects.all()

        query = request.GET.get('q', '')
        status = request.GET.get('status', '')
        comex = request.GET.get('comex', '')
        modal = request.GET.get('modal', '')
        empresa_tipo = request.GET.get('empresa_tipo', '')

        if status:
            processos = processos.filter(status=status)

        if comex:
            processos = processos.filter(comex=comex)

        if modal:
            processos = processos.filter(modal=modal)

        if empresa_tipo:
            processos = processos.filter(empresa_tipo_id=empresa_tipo)

        default_page = 1
        page = request.GET.get('page', default_page)
        processos_per_page = 25

        paginator = Paginator(processos, processos_per_page)
        page_number = request.GET.get('page')
        processos_page = paginator.get_page(page_number)

        try:
            processos_page = paginator.page(page)
        except PageNotAnInteger:
            processos_page = paginator.page(default_page)
        except EmptyPage:
            processos_page = paginator.page(paginator.num_pages)

        return render(request, PComex1View.template_name, {
            'title': title,
            'processos': processos_page,
            'tipos_comex': tipos_comex,
            'query': query,
            'status': status,
            'comex': comex,
            'modal': modal,
            'empresa_tipo': empresa_tipo,
            'form': form
        })


class PComex2View(View):
    template_name = 'processos/comex/comex_em_andamento.html'

    def get(self, request):
        title = 'COMEX EM ANDAMENTO'
        return render(request, PComex1View.template_name, {
                'title': title
            })


class PComex3View(View):
    template_name = 'processos/comex/comex_a_faturar.html'

    def get(self, request):
        title = 'COMEX A FATURAR'
        return render(request, PComex1View.template_name, {
                'title': title
            })


class PComex4View(View):
    template_name = 'processos/comex/comex_faturado.html'

    def get(self, request):
        title = 'COMEX FATURADO'
        return render(request, PComex1View.template_name, {
                'title': title
            })


class PComex5View(View):
    template_name = 'processos/comex/comex_verificar.html'

    def get(self, request):
        title = 'COMEX VERIFICAR'
        return render(request, PComex1View.template_name, {
                'title': title
            })


class PComex6View(View):
    template_name = 'processos/comex/comex_concluido.html'

    def get(self, request):
        title = 'COMEX CONCLUIDO'
        return render(request, PComex1View.template_name, {
                'title': title
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


def todo_view(request, id):
    title = 'Editar Processo'
    todos = Teste1Cliente.objects.filter(id=id)

    if not todos.exists():
        messages.add_message(request, constants.ERROR, 'Não existe uma tarefa com este identificador !!!')
        return redirect('/')

    todo = Teste1Cliente.objects.get(id=id)
    context = {'title': title,
               'todo': todo}
    return render(request, 'processos/processos_comex_update.html', context)


def todo_update(request, id):
    title = 'Alterar Tarefa'

    description = request.POST.get('description')
    category = request.POST.get('category')
    status = request.POST.get('status')

    todo = Teste1Cliente.objects.get(id=id)
    context = {'title': title,
               'todo': todo}

    if (len(description.strip()) == 0):
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos !!!')
        return render(request, 'processos/processos_comex_update.html', context)

    todos = Teste1Cliente.objects.filter(id=id)
    if todos.exists():
        try:
            todo.description = description
            todo.category = category
            todo.status = status

            todo.save()

            messages.add_message(request, constants.SUCCESS, 'Tarefa Alterada com Sucesso!')
            return redirect('/')
        except AttributeError:
            messages.add_message(request, constants.ERROR, 'Erro Interno do Sistema!!!')
            return redirect('/')
