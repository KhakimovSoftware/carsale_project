from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from cars.models import CarModel

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['cars'] = CarModel.objects.filter(is_featured=True).order_by()
        data['cars'] = CarModel.objects.order_by('created_at')
        return data
class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

