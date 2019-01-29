from rest_framework import serializers
from produto.models import Produto
from .models import Compra, Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = ('compra',)


class CompraSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)


    class Meta:
        model = Compra
        fields = ['cliente', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        compra = Compra.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(compra=compra, **item_data)
        return compra
