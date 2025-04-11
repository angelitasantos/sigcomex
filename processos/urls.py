from django.urls import path
from . import views
from .views import (ProcessosTemplateView, ProcessoComexView,
                    ProcessoServicoView, ProcessoNextBHView,
                    ProcessoNextSPView, ProcessoLeanView)

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
]
