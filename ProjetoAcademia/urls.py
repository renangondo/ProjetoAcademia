from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/landing/', permanent=False)),  # << redireciona / para /landing/
    path('', include('paginas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('medidas/', include('medidas.urls')),
    path('', include('treino.urls')),
]
