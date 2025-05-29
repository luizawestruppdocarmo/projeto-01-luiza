from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} ({self.sigla})'

class Cidade(models.Model):
    nome = models.CharField(max_length=80)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.nome} ({self.estado.sigla})'

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    data_nasc = models.DateField()
    email = models.EmailField(max_length=200)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} - {self.email}'
