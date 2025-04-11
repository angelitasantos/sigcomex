from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from parceiros.models import (Teste1Cliente)
from parceiros.forms import (ClienteForm)
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
