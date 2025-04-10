from django.urls import path
from .views import (SuporteTemplateView, EmpresaView, UsuarioView,
                    ExportarDadosView, ImportarDadosView,
                    ImportarClienteView, ImportarClienteAlteradoView,
                    ImportarProcessoView, ImportarProcessoAlteradoView)


urlpatterns = [
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
