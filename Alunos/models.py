from django.db import models

# Tabela Aluno
class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True, null=True, blank=True)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=255, null=True, blank=True)
    responsavel = models.ForeignKey('Responsavel', on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Responsavel
    photo = models.ImageField(upload_to='Alunos/', blank=True, null=True)

    def __str__(self):
        return self.nome

# Tabela Responsavel
class Responsavel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

# Tabela Matricula
class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    alunos_idalunos = models.IntegerField()  # Exemplo sem FK para a tabela Aluno
    descricao = models.TextField()
    data_matricula = models.DateField()

    def __str__(self):
        return f"Matricula {self.id_matricula}"

# Tabela Doadores
class Doadores(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255)
    cpf_cnpj = models.CharField(max_length=18, unique=True)  # Para CPF ou CNPJ

    def __str__(self):
        return self.nome

# Tabela Doações (com ligação com Doadores)
class Doacao(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    doador = models.ForeignKey(Doadores, on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Doadores

    def __str__(self):
        return f"Doação {self.id}"

# Tabela Curso
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    periodo = models.CharField(max_length=50)
    dia_aula = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao

# Tabela Visitas (com ligação com Aluno)
class Visitas(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Aluno

    def __str__(self):
        return self.nome

# Tabela Agendamento (com ligação com Aluno)
class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Aluno

    def __str__(self):
        return f"Agendamento {self.id}"

# Tabela Presença
class Presenca(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    data_presenca = models.DateField()

    def __str__(self):
        return f"Presença {self.id} em {self.data_presenca}"

# Tabela Encaminha (com ligação com Aluno e Assistente)
class Encaminha(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField()
    aluno = models.ForeignKey(Aluno, on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Aluno
    assistente = models.ForeignKey('Assistente', on_delete=models.SET_NULL, null=True, blank=True)  # Ligação com Assistente

    def __str__(self):
        return f"Encaminhamento {self.id}"

# Tabela Assistente
class Assistente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
