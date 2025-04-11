from django.views.generic.base import TemplateView


class HomepageTemplateView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PLENO COMEX'
        return context


class OperacionalTemplateView(TemplateView):
    template_name = 'operacional.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'OPERACIONAL'
        return context
