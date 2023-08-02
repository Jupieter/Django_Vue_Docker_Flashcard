from rest_framework import routers,serializers,viewsets
from cards.models import CardSets
from django.contrib.auth.models import User


class CardSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardSets
        fields = ['id', 'set_name', 'set_description', 'checked']


class CardSetPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardSets
        fields = ['set_name', 'set_description']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', ]