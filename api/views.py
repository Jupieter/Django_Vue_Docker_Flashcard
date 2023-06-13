from rest_framework import permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import JsonResponse
# API definition for card_set
from .serializers import CardSetSerializer, CardSetPostSerializer, UserSerializer
# CardSets model
from cards.models import CardSets


@csrf_exempt
def card_set(request):
    '''
    List all card_set snippets
    '''
    if(request.method == 'GET'):
        # get all the card_set
        card_set = CardSets.objects.all()
        serializer = CardSetSerializer(card_set, many=True)
        return JsonResponse(serializer.data,safe=False)

@api_view(['POST'])
def create_card_set(request):
    data=request.data
    err = "error"
    print(data)
    serializer = CardSetPostSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(err, status=400)

@api_view(['DELETE'])
def delete_card_set(request, pk):
    print("pk:  ", pk)
    try:
        card_set = CardSets.objects.get(pk=pk)
        print(card_set)
        card_set.delete()
        return Response({'message': 'Checked value deleted successfully.'}, status=204)  # Sikeres törlés, üres válasz (No Content)
    except CardSets.DoesNotExist:
        return Response({'message': 'CardSets not found.'},status=404)  # Nem található az adott ID-val rendelkező 

@api_view(['POST'])
def update_cardset(request, pk):
    try:
        cardset = CardSets.objects.get(pk=pk)
        print(cardset)
        if request.method == 'POST':
            set_name = request.data.get('set_name')
            set_description = request.data.get('set_description')
            cardset.set_name = set_name
            cardset.set_description = set_description
            cardset.save()
            return JsonResponse({'message': 'CardSet updated successfully.'})

    except CardSets.DoesNotExist:
        return JsonResponse({'error': 'CardSet does not exist.'})

    return JsonResponse({'error': 'Invalid request method.'})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def cardset_checked_view(request, pk):
    print("pk:  ", pk)
    try:
        card_set = CardSets.objects.get(pk=pk)
        print(card_set)
        card_set.checked = not card_set.checked  # Toggle the checked value
        card_set.save()
        return Response({'message': 'Checked value updated successfully.'})
    except CardSets.DoesNotExist:
        return Response({'message': 'CardSets not found.'}, status=404)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = make_password(serializer.validated_data['password'])
        user = User.objects.create(username=serializer.validated_data['username'], email=email, password=password)
        _, token = AuthToken.objects.create(user)
        return Response({'user': UserSerializer(user).data, 'token': token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # username = request.data.get('username')
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user.id)
        if user is not None:
            login(request, user)
            return super().post(request, format=None)
        return Response({'error': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(KnoxLogoutView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return super().post(request, format=None)