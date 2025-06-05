from django.urls import path
from .views import IndexView


# path('endereço', minhaView.as_view(), name='nome_da_view')

urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
]