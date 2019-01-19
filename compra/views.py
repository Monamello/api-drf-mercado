from rest_framework import status, viewsets
from django.shortcuts import render
from .serializer import CompraSerializer
from .models import Compra 
from produto.models import Produto


class CompraViewSet(viewsets.ModelViewSet):
    model = Compra
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def get_queryset(self):
        return Compra.objects.filter(cliente=self.request.user)

