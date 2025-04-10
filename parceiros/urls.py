from django.urls import path
from .views import (ParceiroView, ClienteView, CategoriaView, GrupoView)


urlpatterns = [
     path('parceiros/', ParceiroView.as_view(), name='parceiros'),
     path('clientes/', ClienteView.as_view(), name='clientes'),
     path('categorias/', CategoriaView.as_view(), name='categorias'),
     path('grupos/', GrupoView.as_view(), name='grupos'),
]
