from django.urls import path
from .views import IndexView, LandingPageView


# path('endereço', minhaView.as_view(), name='nome_da_view')

urlpatterns = [
    path('home/', IndexView.as_view(), name='index'),
    path('landing/', LandingPageView.as_view(), name='landing_page'),
]