from django.urls import path
from .views import HomePageView, AboutView, ServiceView, CarDetailView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('serivce/', ServiceView.as_view(), name='service'),
    path('<int:pk>/detail/', CarDetailView.as_view(), name='detail')
]