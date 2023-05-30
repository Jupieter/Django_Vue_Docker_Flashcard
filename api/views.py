from django.shortcuts import render

# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# for sending response to the client
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
# API definition for card_set
from .serializers import CardSetSerializer, CardSetPostSerializer
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
    
    elif(request.method == 'POST'):
        # parse the incoming information
        print("request --->", request)
        data = JSONParser().parse(request)
        # print(data)
        # instanciate with the serializer
        # serializer = CardSetSerializer(data=data)
        # check if the sent information is okay
        # if(serializer.is_valid()):
            # if okay, save it on the database
        #    serializer.save()
            # provide a Json Response with the data that was saved
        #    return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        # return JsonResponse(serializer.errors, status=400)

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
        return Response(status=204)  # Sikeres törlés, üres válasz (No Content)
    except CardSets.DoesNotExist:
        return Response(status=404)  # Nem található az adott ID-val rendelkező rekord