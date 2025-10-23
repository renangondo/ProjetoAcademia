from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, LandingPageView

urlpatterns = [
    path('home/', IndexView.as_view(), name='index'),
    path('landing/', LandingPageView.as_view(), name='landing_page'),

    # urls de autenticação
    path('login/', auth_views.LoginView.as_view(template_name='paginas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='paginas/logout.html', next_page='login'), name='logout'),
]
