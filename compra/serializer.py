from rest_framework import serializers
from .models import Compra


class CompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Compra
        fields = ('cliente', 'produtos', 'quantidade',)

    def create(self, validated_data):
        request = self.context['request']
        invitation = request.data.get('produtos')
        print("@@@@@@@@@@@@")
        print(invitation)
        return invitation