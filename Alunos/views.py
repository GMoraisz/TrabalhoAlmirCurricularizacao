from Alunos.models import Aluno
from Alunos.forms import AlunoModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class AlunosListView(ListView):
    model = Aluno
    template_name = 'alunos.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        alunos = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')
        if search:
            alunos = alunos.filter(nome__icontains=search)
        return alunos


class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'Aluno_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewAlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoModelForm
    template_name = 'new_aluno.html'
    success_url = reverse_lazy('alunos_list')


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoModelForm
    template_name = 'Aluno_update.html'

    def get_success_url(self):
        return reverse_lazy('Aluno_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'Aluno_delete.html'
    success_url = reverse_lazy('Alunos_list')
