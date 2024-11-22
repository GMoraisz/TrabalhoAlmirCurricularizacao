from django import forms
from Alunos.models import Aluno


class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno  # Corrigido: era 'nome', deveria ser 'model'
        fields = '__all__'  # Inclui todos os campos do modelo

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf and Aluno.objects.filter(cpf=cpf).exists():
            self.add_error('cpf', 'Já existe um aluno com este CPF.')
        return cpf

    def clean_nascimento(self):
        nascimento = self.cleaned_data.get('nascimento')
        if nascimento and nascimento.year < 1900:
            self.add_error('nascimento', 'Ano de nascimento inválido.')
        return nascimento

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome and len(nome.split()) < 2:
            self.add_error('nome', 'O nome completo deve incluir pelo menos um sobrenome.')
        return nome

    def clean_idade(self):
        idade = self.cleaned_data.get('idade')
        if idade is not None and idade < 0:
            self.add_error('idade', 'O campo "idade" não pode ser negativo.')
        return idade
