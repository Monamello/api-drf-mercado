from rest_framework import status, viewsets
from django.shortcuts import render
from .serializer import CompraSerializer
from .models import Compra 
from produto.models import Produto


class CompraViewSet(viewsets.ModelViewSet):
    model = Compra
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    # def create(self, validated_data):
    #     compra = validated_data.get('produtos')
    #     print("@@@@@@@@@@@@")
    #     print(compra)
    #     return super().create(request)

