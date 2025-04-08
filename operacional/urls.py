from django.urls import path
from .views import (HomepageTemplateView, ClienteView, CategoriaView,
                    GrupoView, SuporteTemplateView, ImportarDadosView,
                    ImportarClienteView, ImportarClienteAlteradoView,
                    ImportarProcessoView, ImportarProcessoAlteradoView,
                    OperacionalTemplateView, ProcessosTemplateView)

urlpatterns = [
     path('', HomepageTemplateView.as_view(), name='homepage'),

     path('clientes/', ClienteView.as_view(), name='clientes'),
     path('categorias/', CategoriaView.as_view(), name='categorias'),
     path('grupos/', GrupoView.as_view(), name='grupos'),

     path('processos/', ProcessosTemplateView.as_view(), name='processos'),
     path('operacional/', OperacionalTemplateView.as_view(), name='operacional'),

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
