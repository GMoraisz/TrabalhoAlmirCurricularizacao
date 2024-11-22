from django import forms
from Alunos.models import Aluno


class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'  # Isso vai incluir todos os campos do modelo Aluno

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Aluno.objects.filter(cpf=cpf).exists():
            self.add_error('cpf', 'Já existe um aluno com este CPF.')
        return cpf

    def clean_nascimento(self):
        nascimento = self.cleaned_data.get('nascimento')
        if nascimento.year < 1900:  # Exemplo de validação para a data de nascimento
            self.add_error('nascimento', 'Ano de nascimento inválido.')
        return nascimento

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome.split()) < 2:  # Exemplo: o nome deve ter pelo menos um sobrenome
            self.add_error('nome', 'O nome completo deve incluir pelo menos um sobrenome.')
        return nome
