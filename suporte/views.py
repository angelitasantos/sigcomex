from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from parceiros.models import (Teste1Cliente)
from parceiros.forms import (ClienteForm)
from .forms import (ImportarDadosForm)
from django.contrib import messages
from django.db.models import Q
import pandas as pd
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger,
                                   )

from django.http import HttpResponse
from io import BytesIO

MODELOS_DISPONIVEIS = {
    'Clientes': Teste1Cliente,
}


class SuporteTemplateView(TemplateView):
    template_name = 'suporte/suporte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SUPORTE'
        return context


class ExportarDadosView(TemplateView):
    template_name = 'suporte/exportar_excel.html'

    def get(self, request, *args, **kwargs):
        title = 'EXPORTAR DADOS'
        context = {'modelos': MODELOS_DISPONIVEIS.keys(), 'title': title}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        nome_modelo = request.POST.get('tabela')
        modelo = MODELOS_DISPONIVEIS.get(nome_modelo)

        if modelo is None:
            return HttpResponse("Modelo inválido", status=400)

        queryset = modelo.objects.all().values()
        df = pd.DataFrame(list(queryset))

        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name=nome_modelo)

        buffer.seek(0)

        t = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response = HttpResponse(
            buffer,
            content_type=t
        )
        arquivo = f'attachment; filename="{nome_modelo}.xlsx"'
        response['Content-Disposition'] = arquivo
        return response


class ImportarDadosView(TemplateView):
    template_name = 'suporte/importar_dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'IMPORTAR DADOS'
        return context


class ImportarClienteView(TemplateView):
    template_name = 'suporte/importar_clientes.html'

    def get(self, request):
        title = 'IMPORTAR CLIENTES'
        clientes = Teste1Cliente.objects.all().order_by('-id')[:50]
        form = ImportarDadosForm()
        return render(request, self.template_name, {
            'title': title,
            'form': form,
            'clientes': clientes
        })

    def post(self, request):
        form = ImportarDadosForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = request.FILES['arquivo']
            df = pd.read_excel(arquivo)
            for _, row in df.iterrows():
                self.criar_cliente(row)
            return redirect('importarclientes')
        messages.success(request, 'Clientes Importados com Sucesso !')
        return render(request, self.template_name, {'form': form})

    def criar_cliente(self, row):
        Teste1Cliente.objects.get_or_create(
            cnpj=row['cnpj'],
            defaults={
                'nome': row['nome'],
                'razao_social': row['razao_social'],
                'insc_est': row['insc_est'],
                'sigla_imp': row['sigla_imp'],
                'sigla_exp': row['sigla_exp'],
                'serv_sigla_imp': row['serv_sigla_imp'],
                'serv_sigla_exp': row['serv_sigla_exp'],
                'cod_interno': row['cod_interno'],
                'observacoes': row['observacoes'],
                'grupo_id': row['grupo_id'],
                'categoria_id': row['categoria_id'],
                'status': row['status']
            }
        )


class ImportarClienteAlteradoView(TemplateView):
    template_name = 'suporte/importar_clientes_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'IMPORTAR CLIENTES ALTERADOS'
        return context


class ImportarProcessoView(TemplateView):
    template_name = 'suporte/importar_processos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'IMPORTAR PROCESSOS'
        return context


class ImportarProcessoAlteradoView(TemplateView):
    template_name = 'suporte/importar_processos_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'IMPORTAR PROCESSOS ALTERADOS'
        return context


class EmpresaView(View):
    template_name = 'suporte/empresas.html'

    def get(self, request):
        title = 'EMPRESAS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=1)
        form = ClienteForm()

        return render(request, EmpresaView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class UsuarioView(View):
    template_name = 'suporte/usuarios.html'

    def get(self, request):
        title = 'USUARIOS'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, UsuarioView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })
