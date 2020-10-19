from django.urls import path
from home.views import home_inicio

urlpatterns = [
    path('', home_inicio, name = 'home_inicio')
]
