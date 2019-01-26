from rest_framework import serializers
from produto.models import Produto
from .models import Compra, Item


class CompraSerializer(serializers.ModelSerializer):
    items = serializers.SlugRelatedField(
        many=True,
        slug_field='nome',
        queryset=Item.objects.filter()
     )

    class Meta:
        model = Compra
        fields = '__all__'

    def create(self, validated_data):
        # produtos = validated_data.get('produtos')
        # quantidade = validated_data.get('quantidade')

        # for produto in produtos:
        #     if not quantidade > produto.estoque:
        #         produto.estoque -= quantidade
        #         produto.save()
        #         print(produto.estoque)
        #     else:
        #         message = 'Quantidade do produto não tem em estoque!'
        #         raise serializers.ValidationError(message)

            
        return super(CompraSerializer, self).create(validated_data)