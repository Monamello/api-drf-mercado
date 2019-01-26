from django.db import models
from compra.models import Compra

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    estoque = models.PositiveIntegerField()
    quant_comprada = models.IntegerField()

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super(Produto, self).save(*args, **kwargs)