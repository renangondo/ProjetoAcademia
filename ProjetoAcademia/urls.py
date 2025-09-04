from django.contrib import admin
from django.urls import path, include


# Importa todas as URLS criadas  no app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('usuarios/' , include('usuarios.urls')),
]
