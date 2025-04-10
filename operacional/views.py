from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import (Teste1Categoria, Teste1Cliente, Teste1Grupo)
from .forms import (ClienteForm, CategoriaForm, GrupoForm, ImportarDadosForm)
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
    'Categorias': Teste1Categoria,
    'Grupos': Teste1Grupo,
}


class HomepageTemplateView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PLENO COMEX'
        return context


class SuporteTemplateView(TemplateView):
    template_name = 'suporte/suporte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SUPORTE'
        return context


class ProcessosTemplateView(TemplateView):
    template_name = 'processos/processos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PROCESSOS'
        return context


class OperacionalTemplateView(TemplateView):
    template_name = 'operacional/operacional.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OPERACIONAL'
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


class ParceiroView(View):
    template_name = 'clientes/parceiros_list.html'

    def get(self, request):
        title = 'PARCEIROS'
        form = ClienteForm()
        clientes = Teste1Cliente.objects.all().order_by('nome')
        grupos = Teste1Grupo.objects.all()
        categorias = Teste1Categoria.objects.all()

        query = request.GET.get('q', '')
        status = request.GET.get('status', '')
        grupo = request.GET.get('grupo', '')
        categoria = request.GET.get('categoria', '')

        if status:
            clientes = clientes.filter(status=status)

        if grupo:
            clientes = clientes.filter(grupo__id=grupo)

        if categoria:
            clientes = clientes.filter(categoria__id=categoria)

        default_page = 1
        page = request.GET.get('page', default_page)
        clientes_per_page = 25

        paginator = Paginator(clientes, clientes_per_page)
        page_number = request.GET.get('page')
        clientes_page = paginator.get_page(page_number)

        try:
            clientes_page = paginator.page(page)
        except PageNotAnInteger:
            clientes_page = paginator.page(default_page)
        except EmptyPage:
            clientes_page = paginator.page(paginator.num_pages)

        return render(request, ParceiroView.template_name, {
            'title': title,
            'clientes': clientes_page,
            'categorias': categorias,
            'query': query,
            'status': status,
            'grupos': grupos,
            'categoria': categoria,
            'form': form
        })

    def post(self, request):
        title = 'PARCEIROS'
        form = ClienteForm()

        nome = request.POST.get('nome')
        razao_social = request.POST.get('razao_social')
        cnpj = request.POST.get('cnpj')
        insc_est = request.POST.get('insc_est')
        sigla_imp = request.POST.get('sigla_imp')
        sigla_exp = request.POST.get('sigla_exp')
        serv_sigla_imp = request.POST.get('serv_sigla_imp')
        serv_sigla_exp = request.POST.get('serv_sigla_exp')
        cod_interno = request.POST.get('cod_interno')
        observacoes = request.POST.get('observacoes')
        grupo1 = request.POST.get('grupo_id')
        categoria1 = request.POST.get('categoria_id')

        grupo = 1 if grupo1 is None else grupo1
        categoria = 1 if grupo1 is None else categoria1

        status = 'A'
        if request.method == 'POST' and 'create' in request.POST:

            Teste1Cliente.objects.create(
                nome=nome,
                razao_social=razao_social,
                cnpj=cnpj,
                insc_est=insc_est,
                sigla_imp=sigla_imp,
                sigla_exp=sigla_exp,
                serv_sigla_imp=serv_sigla_imp,
                serv_sigla_exp=serv_sigla_exp,
                cod_interno=cod_interno,
                observacoes=observacoes,
                status=status,
                grupo_id=grupo,
                categoria_id=categoria
            )

            msg = f'Parceiro {nome} Incluído com Sucesso !'
            messages.success(request, msg)
            return redirect('parceiros')

        elif request.method == 'POST' and 'update' in request.POST:
            id = request.POST.get('id')
            status = request.POST.get('status')
            grupo = request.POST.get('grupo_id')
            categoria = request.POST.get('categoria_id')
            cliente = get_object_or_404(Teste1Cliente, pk=id)

            cliente.nome = nome
            cliente.razao_social = razao_social
            cliente.cnpj = cnpj
            cliente.insc_est = insc_est
            cliente.sigla_imp = sigla_imp
            cliente.sigla_exp = sigla_exp
            cliente.serv_sigla_imp = serv_sigla_imp
            cliente.serv_sigla_exp = serv_sigla_exp
            cliente.cod_interno = cod_interno
            cliente.observacoes = observacoes
            cliente.status = status
            cliente.grupo_id = grupo
            cliente.categoria_id = categoria
            cliente.save()
            msg = f'Parceiro {nome} Alterado com Sucesso !'
            messages.success(request, msg)
            return redirect('parceiros')

        elif request.method == 'POST' and 'search' in request.POST:
            query = request.POST.get('q', '')
            status = request.POST.get('status', '')
            grupo = request.POST.get('grupo', '')
            categoria = request.POST.get('categoria', '')

            clientes = Teste1Cliente.objects.all()
            grupos = Teste1Grupo.objects.all()
            categorias = Teste1Categoria.objects.all()

            if status:
                clientes = clientes.filter(status=status)

            if grupo:
                clientes = clientes.filter(grupo__id=grupo)

            if categoria:
                clientes = clientes.filter(categoria__id=categoria)

            if query:
                clientes = clientes.filter(
                    Q(nome__icontains=query) |
                    Q(cnpj__icontains=query) |
                    Q(sigla_imp__icontains=query) |
                    Q(sigla_exp__icontains=query) |
                    Q(serv_sigla_imp__icontains=query) |
                    Q(serv_sigla_exp__icontains=query) |
                    Q(razao_social__icontains=query)
                    )

            return render(request, ParceiroView.template_name, {
                'title': title,
                'clientes': clientes,
                'status': status,
                'grupo': grupo,
                'categoria': categoria,
                'grupos': grupos,
                'categorias': categorias,
                'form': form
            })

        elif request.method == 'POST' and 'delete' in request.POST:
            id = request.POST.get('id')
            cliente = get_object_or_404(Teste1Cliente, pk=id)
            # Teste1Cliente.objects.get(id=id).delete()
            msg = f'Parceiro {cliente.nome} Excluído com Sucesso !'
            messages.success(request, msg)
            return redirect('parceiros')


class ClienteView(View):
    template_name = 'clientes/clientes_list.html'

    def get(self, request):
        title = 'CLIENTES'
        form = ClienteForm()
        clientes = Teste1Cliente.objects.all().order_by('nome').filter(
                status='A', grupo_id=3)
        grupos = Teste1Grupo.objects.all()
        categorias = Teste1Categoria.objects.all()

        query = request.GET.get('q', '')
        status = request.GET.get('status', '')
        grupo = request.GET.get('grupo', '')
        categoria = request.GET.get('categoria', '')

        if status:
            clientes = clientes.filter(status=status)

        if grupo:
            clientes = clientes.filter(grupo__id=grupo)

        if categoria:
            clientes = clientes.filter(categoria__id=categoria)

        default_page = 1
        page = request.GET.get('page', default_page)
        clientes_per_page = 25

        paginator = Paginator(clientes, clientes_per_page)
        page_number = request.GET.get('page')
        clientes_page = paginator.get_page(page_number)

        try:
            clientes_page = paginator.page(page)
        except PageNotAnInteger:
            clientes_page = paginator.page(default_page)
        except EmptyPage:
            clientes_page = paginator.page(paginator.num_pages)

        return render(request, ClienteView.template_name, {
            'title': title,
            'clientes': clientes_page,
            'categorias': categorias,
            'query': query,
            'status': status,
            'grupos': grupos,
            'categoria': categoria,
            'form': form
        })

    def post(self, request):
        title = 'CLIENTES'
        form = ClienteForm()
        categoria1 = request.POST.get('categoria_id')
        categoria = 1 if categoria1 is None else categoria1

        if request.method == 'POST' and 'search' in request.POST:
            query = request.POST.get('q', '')
            categoria = request.POST.get('categoria', '')

            clientes = Teste1Cliente.objects.all().filter(
                status='A', grupo_id=3)
            categorias = Teste1Categoria.objects.all()

            if categoria:
                clientes = clientes.filter(categoria__id=categoria)

            if query:
                clientes = clientes.filter(
                    Q(nome__icontains=query) |
                    Q(cnpj__icontains=query) |
                    Q(sigla_imp__icontains=query) |
                    Q(sigla_exp__icontains=query) |
                    Q(serv_sigla_imp__icontains=query) |
                    Q(serv_sigla_exp__icontains=query) |
                    Q(razao_social__icontains=query)
                    )

            return render(request, ClienteView.template_name, {
                'title': title,
                'clientes': clientes,
                'categoria': categoria,
                'categorias': categorias,
                'form': form
            })


class CategoriaView(View):
    template_name = 'clientes/categorias_list.html'

    def get(self, request):
        title = 'CATEGORIAS'
        categorias = Teste1Categoria.objects.all().order_by('nome')
        form = CategoriaForm()

        return render(request, CategoriaView.template_name, {
            'title': title,
            'categorias': categorias,
            'form': form
        })

    def post(self, request):
        if request.method == 'POST' and 'create' in request.POST:
            nome = request.POST.get('nome')
            status = 'A'

            Teste1Categoria.objects.create(
                nome=nome,
                status=status
            )

            msg = f'Categoria {nome} Incluída com Sucesso !'
            messages.success(request, msg)
            return redirect('categorias')

        elif request.method == 'POST' and 'update' in request.POST:
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            status = request.POST.get('status')
            categoria = get_object_or_404(Teste1Categoria, pk=id)

            categoria.nome = nome
            categoria.status = status
            categoria.save()
            msg = f'Categoria {nome} Alterada com Sucesso !'
            messages.success(request, msg)
            return redirect('categorias')

        elif request.method == 'POST' and 'delete' in request.POST:
            id = request.POST.get('id')
            categoria = get_object_or_404(Teste1Categoria, pk=id)
            # Teste1Categoria.objects.get(id=id).delete()
            msg = f'Categoria {categoria.nome} Excluída com Sucesso !'
            messages.success(request, msg)
            return redirect('categorias')


class GrupoView(View):
    template_name = 'clientes/grupos_list.html'

    def get(self, request):
        title = 'GRUPOS'
        grupos = Teste1Grupo.objects.all().order_by('nome')
        form = GrupoForm()

        return render(request, GrupoView.template_name, {
            'title': title,
            'grupos': grupos,
            'form': form
        })

    def post(self, request):
        if request.method == 'POST' and 'create' in request.POST:
            nome = request.POST.get('nome')
            status = 'A'

            Teste1Grupo.objects.create(
                nome=nome,
                status=status
            )

            msg = f'Grupo {nome} Incluído com Sucesso !'
            messages.success(request, msg)
            return redirect('grupos')

        elif request.method == 'POST' and 'update' in request.POST:
            id = request.POST.get('id')
            nome = request.POST.get('nome')
            status = request.POST.get('status')
            grupo = get_object_or_404(Teste1Grupo, pk=id)

            grupo.nome = nome
            grupo.status = status
            grupo.save()
            msg = f'Grupo {nome} Alterado com Sucesso !'
            messages.success(request, msg)
            return redirect('grupos')

        elif request.method == 'POST' and 'delete' in request.POST:
            id = request.POST.get('id')
            grupo = get_object_or_404(Teste1Grupo, pk=id)
            # Teste1Grupo.objects.get(id=id).delete()
            msg = f'Grupo {grupo.nome} Excluído com Sucesso !'
            messages.success(request, msg)
            return redirect('grupos')


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


class HonorarioView(View):
    template_name = 'operacional/honorarios.html'

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
    template_name = 'operacional/tipos_servicos.html'

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


class SdaView(View):
    template_name = 'operacional/sda.html'

    def get(self, request):
        title = 'SDAs'
        clientes = Teste1Cliente.objects.all().order_by(
            'nome').filter(grupo_id=4)
        form = ClienteForm()

        return render(request, SdaView.template_name, {
            'title': title,
            'clientes': clientes,
            'form': form
        })


class OutroView(View):
    template_name = 'operacional/outros.html'

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


class ProcessoComexView(View):
    template_name = 'processos/processos comex.html'

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
    template_name = 'processos/processos servicos.html'

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


class FaturamentoView(View):
    template_name = 'processos/faturamento.html'

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
    template_name = 'processos/notas_fiscais.html'

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
