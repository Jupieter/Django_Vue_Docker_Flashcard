from rest_framework import routers,serializers,viewsets
from cards.models import CardSets


class CardSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardSets
        fields = ['id', 'set_name', 'set_description', 'checked']


class CardSetPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardSets
        fields = ['set_name', 'set_description']