from django.shortcuts import render

# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for card_set
from .serializers import CardSetSerializer
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
        # serialize the card_set data
        serializer = CardSetSerializer(card_set, many=True)
        # return a Json response
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