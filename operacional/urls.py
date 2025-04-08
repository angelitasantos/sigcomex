from django.urls import path
from .views import (HomepageTemplateView, ClienteView, CategoriaView,
                    GrupoView, SuporteTemplateView, ImportarDadosView,
                    ImportarClienteView, ImportarProcessoView,
                    ImportarProcessoAlteradoView)

urlpatterns = [
    path('', HomepageTemplateView.as_view(), name='homepage'),

    path('clientes/', ClienteView.as_view(), name='clientes'),
    path('categorias/', CategoriaView.as_view(), name='categorias'),
    path('grupos/', GrupoView.as_view(), name='grupos'),

    path('suporte/', SuporteTemplateView.as_view(), name='suporte'),

    path('importardados/',
         ImportarDadosView.as_view(),
         name='importardados'),

    path('importarclientes/',
         ImportarClienteView.as_view(),
         name='importarclientes'),
    path('importarprocessos/',
         ImportarProcessoView.as_view(),
         name='importarprocessos'),
    path('importarprocessosalterados/',
         ImportarProcessoAlteradoView.as_view(),
         name='importarprocessosalterados'),
]
