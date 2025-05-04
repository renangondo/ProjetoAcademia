from django.urls import path
from .views import indexView


# path('endereço', minhaView.as_view(), name='nome_da_view')

urlpatterns = [
    path('inicio/', indexView.as_view(), name='inicio'), 
]