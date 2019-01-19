from rest_framework import serializers
from produto.models import Produto
from .models import Compra


class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ('cliente', 'produtos', 'quantidade',)

    def create(self, validated_data):
        produtos = validated_data.get('produtos')
        quantidade = validated_data.get('quantidade')
        for produto in produtos:
            produto.estoque -= quantidade
            produto.save()
            print(produto.estoque)

        return super(CompraSerializer, self).create(validated_data)