from django.urls import path
from .views import (FaturamentoView, HonorarioView,
                    NotaFiscalView,
                    OutroView, ControleSdaView,
                    TipoServicoView)

urlpatterns = [
     path('honorarios/', HonorarioView.as_view(), name='honorarios'),
     path('tiposservicos/', TipoServicoView.as_view(), name='tipos_servicos'),
     path('faturamento/', FaturamentoView.as_view(), name='faturamento'),
     path('controlesda/', ControleSdaView.as_view(), name='controle_sda'),
     path('notasfiscais/', NotaFiscalView.as_view(), name='notas_fiscais'),
     path('notasdebito/', OutroView.as_view(), name='notas_debito'),
]
