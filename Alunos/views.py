from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from Alunos.models import Aluno
from Alunos.forms import AlunoModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Função de logout
@login_required(login_url='login')  # Garante que o usuário esteja logado antes de deslogar
def logout_view(request):
    logout(request)  # Finaliza a sessão do usuário
    return redirect('login')  # Redireciona para a página de login após o logout


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlunosListView(ListView):
    model = Aluno
    template_name = 'Alunos.html'
    context_object_name = 'Alunos'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(nome__icontains=search)
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class AlunoDetailView(DetailView):
    model = Aluno
    template_name = 'Aluno_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewAlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoModelForm
    template_name = 'new_Aluno.html'
    success_url = reverse_lazy('Alunos_list')


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
