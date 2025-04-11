from django.urls import path
from . import views
from .views import (ProcessosTemplateView, ProcessoComexView,
                    ProcessoServicoView, ProcessoNextBHView,
                    ProcessoNextSPView, ProcessoLeanView,
                    PComex1View, PComex2View, PComex3View,
                    PComex4View, PComex5View, PComex6View)

urlpatterns = [
     path('processos/', ProcessosTemplateView.as_view(), name='processos'),
     path('processoscomex/',
          ProcessoComexView.as_view(), name='processos_comex'),
     path('processosservicos/',
          ProcessoServicoView.as_view(), name='processos_servicos'),
     path('processosnextbh/',
          ProcessoNextBHView.as_view(), name='processos_nextbh'),
     path('processosnextsp/',
          ProcessoNextSPView.as_view(), name='processos_nextsp'),
     path('processoslean/',
          ProcessoLeanView.as_view(), name='processos_lean'),

     path('view/<int:id>', views.todo_view, name='todo_view'),
     path('update/<int:id>', views.todo_update, name='todo_update'),

     path('processoscomex1/',
          PComex1View.as_view(), name='processos_comex1'),
     path('processoscomex2/',
          PComex2View.as_view(), name='processos_comex2'),
     path('processoscomex3/',
          PComex3View.as_view(), name='processos_comex3'),
     path('processoscomex4/',
          PComex4View.as_view(), name='processos_comex4'),
     path('processoscomex5/',
          PComex5View.as_view(), name='processos_comex5'),
     path('processoscomex6/',
          PComex6View.as_view(), name='processos_comex6'),

]
