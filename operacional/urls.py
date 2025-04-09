from django.urls import path
from .views import (HomepageTemplateView, ClienteView, CategoriaView,
                    GrupoView, SuporteTemplateView, ImportarDadosView,
                    ImportarClienteView, ImportarClienteAlteradoView,
                    ImportarProcessoView, ImportarProcessoAlteradoView,
                    OperacionalTemplateView, ProcessosTemplateView,
                    ParceiroView, exportar_excel_view, ExportarDadosView)

urlpatterns = [
     path('', HomepageTemplateView.as_view(), name='homepage'),

     path('exportarexcel/', exportar_excel_view, name='exportar_excel'),
     path('exportardados/',
          ExportarDadosView.as_view(), name='exportardados'),

     path('parceiros/', ParceiroView.as_view(), name='parceiros'),
     path('clientes/', ClienteView.as_view(), name='clientes'),
     path('categorias/', CategoriaView.as_view(), name='categorias'),
     path('grupos/', GrupoView.as_view(), name='grupos'),

     path('processos/', ProcessosTemplateView.as_view(), name='processos'),
     path('operacional/',
          OperacionalTemplateView.as_view(), name='operacional'),

     path('suporte/', SuporteTemplateView.as_view(), name='suporte'),

     path('importardados/',
          ImportarDadosView.as_view(),
          name='importardados'),

     path('importarclientes/',
          ImportarClienteView.as_view(),
          name='importarclientes'),
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
