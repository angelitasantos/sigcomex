from django.urls import path
from .views import (HomepageTemplateView, OperacionalTemplateView)

urlpatterns = [
     path('', HomepageTemplateView.as_view(), name='homepage'),
     path('operacional/',
          OperacionalTemplateView.as_view(), name='operacional'),
]
