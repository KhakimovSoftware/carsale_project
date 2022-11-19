from django.shortcuts import render
from django.views.generic import ListView, TemplateView

class CarView(TemplateView):
    template_name = 'cars.html'

