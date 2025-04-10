from django.urls import path
from .views import (FaturamentoView, HomepageTemplateView, ClienteView,
                    CategoriaView, GrupoView, HonorarioView, NotaFiscalView,
                    OutroView, ProcessoComexView, ProcessoServicoView, SdaView,
                    SuporteTemplateView, ImportarDadosView,
                    ImportarClienteView, ImportarClienteAlteradoView,
                    ImportarProcessoView, ImportarProcessoAlteradoView,
                    OperacionalTemplateView, ProcessosTemplateView,
                    ParceiroView, EmpresaView, TipoServicoView, UsuarioView,
                    ExportarDadosView)

urlpatterns = [
     path('', HomepageTemplateView.as_view(), name='homepage'),


     path('parceiros/', ParceiroView.as_view(), name='parceiros'),
     path('clientes/', ClienteView.as_view(), name='clientes'),
     path('categorias/', CategoriaView.as_view(), name='categorias'),
     path('grupos/', GrupoView.as_view(), name='grupos'),

     path('processos/', ProcessosTemplateView.as_view(), name='processos'),
     path('processoscomex/',
          ProcessoComexView.as_view(), name='processos_comex'),
     path('processosservicos/',
          ProcessoServicoView.as_view(), name='processos_servicos'),
     path('faturamento/', FaturamentoView.as_view(), name='faturamento'),
     path('notasfiscais/', NotaFiscalView.as_view(), name='notas_fiscais'),

     path('operacional/',
          OperacionalTemplateView.as_view(), name='operacional'),
     path('honorarios/', HonorarioView.as_view(), name='honorarios'),
     path('tiposservicos/', TipoServicoView.as_view(), name='tipos_servicos'),
     path('sdas/', SdaView.as_view(), name='sdas'),
     path('outros/', OutroView.as_view(), name='outros'),

     path('suporte/', SuporteTemplateView.as_view(), name='suporte'),
     path('empresas/', EmpresaView.as_view(), name='empresas'),
     path('usuarios/', UsuarioView.as_view(), name='usuarios'),

     path('exportardados/',
          ExportarDadosView.as_view(), name='exportardados'),

     path('importardados/',
          ImportarDadosView.as_view(),
          name='importardados'),

     path('importarclientes/',
          ImportarClienteView.as_view(), name='importarclientes'),
     path('importarclientesalterados/',
          ImportarClienteAlteradoView.as_view(),
          name='importarclientesalterados'),
     path('importarprocessos/',
          ImportarProcessoView.as_view(),
          name='importarprocessos'),
     path('importarprocessosalterados/',
          ImportarProcessoAlteradoView.as_view(),
          name='importarprocessosalterados'),
]
