from django.urls import path, include
from .views import CarListView, search

app_name = 'car'

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('search/', search, name='search'),
]