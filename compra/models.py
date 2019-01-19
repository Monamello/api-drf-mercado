from django.db import models
from produto.models import Produto
from django.contrib.auth.models import User


class Compra(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    produtos = models.ManyToManyField('produto.Produto')
    quantidade = models.IntegerField()
