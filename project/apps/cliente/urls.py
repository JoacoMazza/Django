from django.urls import path
from .views import index, crear_cliente


urlpatterns = [
    path('', index , name='home'),
    path('crear/', crear_cliente , name='crar'),
]