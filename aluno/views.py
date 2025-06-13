from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from aluno.models import Aluno
# Create your views here.

class AlunoView(TemplateView):
    template_name = 'alunos/aluno.html'

class AlunoCreateView(CreateView):
    template_name = "alunos/form.html"
    model = Aluno
    success_url = reverse_lazy("aluno")
    fields = ["nome", "idade", "telefone", "email"]
