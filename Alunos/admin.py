from django.contrib import admin
from Alunos.models import (
    Aluno, Responsavel, Matricula, Doadores, Doacao, Curso,
    Visitas, Agendamento, Presenca, Encaminha, Assistente
)

# Configuração do Aluno
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'nascimento', 'endereco', 'responsavel')
    search_fields = ('nome', 'cpf')

# Configuração do Responsavel
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'nascimento', 'endereco', 'telefone')
    search_fields = ('nome', 'cpf')

# Configuração da Matricula
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id_matricula', 'alunos_idalunos', 'descricao', 'data_matricula')
    search_fields = ('descricao',)

# Configuração dos Doadores
class DoadoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'nome', 'endereco', 'cpf_cnpj')
    search_fields = ('nome', 'cpf_cnpj')

# Configuração da Doação
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'doador')
    search_fields = ('descricao',)

# Configuração do Curso
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'periodo', 'dia_aula')
    search_fields = ('descricao',)

# Configuração das Visitas
class VisitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'cpf', 'aluno')
    search_fields = ('nome', 'cpf')

# Configuração do Agendamento
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'aluno')
    search_fields = ('descricao',)

# Configuração da Presença
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'data_presenca')
    search_fields = ('descricao',)

# Configuração do Encaminha
class EncaminhaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'aluno', 'assistente')
    search_fields = ('descricao',)

# Configuração do Assistente
class AssistenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'endereco')
    search_fields = ('nome', 'cpf')

# Registrando os modelos no admin
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Responsavel, ResponsavelAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Doadores, DoadoresAdmin)
admin.site.register(Doacao, DoacaoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Visitas, VisitasAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
admin.site.register(Presenca, PresencaAdmin)
admin.site.register(Encaminha, EncaminhaAdmin)
admin.site.register(Assistente, AssistenteAdmin)
