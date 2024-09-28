from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class EPI(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    prazo_dias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

