from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import CarModel
from django.core.paginator import EmptyPage,Paginator, PageNotAnInteger


class CarListView(ListView):
    queryset = CarModel.objects.all()
    template_name = 'cars.html'
    paginate_by = 2
    page_kwarg = 'car'



def search(request):
    search_cars = CarModel.objects.order_by('-created_at')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            search_cars = search_cars.filter(description__icontains=keyword)

    data = {
        'search_cars': search_cars,

    }
    return render(request, 'search.html', data)



