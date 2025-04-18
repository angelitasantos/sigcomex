from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from .models import (Teste1Categoria, Teste1Cliente, Teste1Grupo)
from .forms import (ClienteForm, CategoriaForm, GrupoForm)
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger,
                                   )


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

            nova_categoria = Teste1Categoria.objects.create(
                nome=nome,
                status=status
            )

            msg = f'{nova_categoria.id} - {nome}!'
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
