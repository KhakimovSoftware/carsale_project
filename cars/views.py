from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import CarModel
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger


class CarListView(ListView):
    queryset = CarModel.objects.all()
    template_name = 'cars.html'
    paginate_by = 6
    page_kwarg = 'car'

    def get_queryset(self):
        qs = CarModel.objects.all()

        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(description__icontains=search)
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['cars'] = CarModel.objects.all()


        return data
