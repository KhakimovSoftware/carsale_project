from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout')
]