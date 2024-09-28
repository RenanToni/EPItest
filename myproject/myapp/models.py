from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class EPIgenerico(models.Model):
    id_lista_fk = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    prazo_dias = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    id_ficha_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE)
    equipamento = models.CharField(max_length=100)
    data_devolucao = models.DateField()
    data_prevista = models.DateField()
    data_emprestimo = models.DateField()
    status = models.CharField(max_length=100)
    condicoes = models.CharField(max_length=100)
    motivo_devolução = models.CharField(max_length=100)
    id_usuario_fk = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class listaEPI(models.Model):
    idCargo_fk = models.ForeignKey(cargo, on_delete=models.CASCADE)
    id_epigenerico_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class produto(models.Model):
    id_epigenerico_fk = models.ForeignKey(EPIgenerico, on_delete=models.CASCADE)
    estoque = models.IntegerField()
    data_validade = models.DateField()
    id_emprestimo_fk = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class usuario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome