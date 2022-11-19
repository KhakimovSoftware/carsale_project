from django.urls import path, include
from .views import CarView

app_name = 'car'

urlpatterns = [
    path('', CarView.as_view(), name='cars'),
]