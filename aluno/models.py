from django.db import models


class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    nascimento = models.DateField()
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'alunos'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome
