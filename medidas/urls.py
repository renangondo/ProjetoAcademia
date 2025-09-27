
from django.urls import path
from .views import MedidasCreate, MedidasUpdate, MedidasDelete  # Adicione esta linha 


# Importa todas as URLS criadas  no app
urlpatterns = [
    path('cadastrar/medidas/', MedidasCreate.as_view(), name='cadastrar_medidas'),
    path('atualizar/medidas/<int:pk>/', MedidasUpdate.as_view(), name='atualizar_medidas'),
    path('excluir/medidas/<int:pk>/', MedidasDelete.as_view(), name='excluir_medidas'),
]
