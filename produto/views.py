from django.shortcuts import render
from .serializer import ProdutoSerializer
from rest_framework import status, viewsets
from .models import Produto


class ProdutoViewSet(viewsets.ModelViewSet):
    model = Produto
    queryset = Produto.objects.filter(estoque__gte = 1)
    serializer_class = ProdutoSerializer