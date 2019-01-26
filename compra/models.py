from django.db import models
from django.contrib.auth.models import User
# from produto.models import Produto


class Compra(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    compra = models.ForeignKey('compra.Compra', related_name='items', on_delete=models.CASCADE)
    produto = models.ForeignKey('produto.Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
