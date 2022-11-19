from django.shortcuts import render
from django.views.generic import TemplateView
from cars.models import CarModel

class HomePageView(TemplateView):
    template_name = 'index.html'
    featured_cars = CarModel.objects.order_by('-created_at').filter(is_featured=True)
    data = {
        'featured_cars': featured_cars,
    }

class AboutView(TemplateView):
    template_name = 'about.html'

class ServiceView(TemplateView):
    template_name = 'service.html'

