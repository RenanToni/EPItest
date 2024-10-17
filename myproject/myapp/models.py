from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome, self.cargo, self.telefone, self.cpf
    
class EPIgenerico(models.Model):    
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    prazo_dias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome, self.descricao, self.prazo_dias

class cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome, self.descricao
    

class Emprestimo(models.Model):
    nome = models.CharField(max_length=100,db_default="")
    condicoes = models.CharField(max_length=100,db_default="")
    status = models.IntegerField(db_default=0)
    data_devolucao = models.DateField(db_default="2020-01-01")
    data_prevista = models.DateField(db_default="2020-01-01")
    data_emprestimo = models.DateField(db_default="2020-01-01")
    motivo_devolução = models.TextField(db_default="2020-01-01")
    id_EPIgenerico_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE, db_default=0)

    def __str__(self):
        return self.nome, self.condicoes, self.status, self.data_prevista, self.id_EPIgenerico_fk

class produto(models.Model):
    id_epigenerico_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE)
    estoque = models.IntegerField()
    data_validade = models.DateField()
    id_emprestimo_fk = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)

    def __str__(self):
        return self.estoque, self.data_validade, self.id_emprestimo_fk
    
class usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.TextField(db_default="")
    senha = models.CharField(max_length=100, db_default="")

    def __str__(self):
        return self.nome, self.email, self.senha