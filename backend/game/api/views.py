import json
import random

from django.template.loader import render_to_string

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from game.api.serializers import (AddUsersSerializer, PlayGameSerializer, FinalResultSerializer)
from game.api.predict_val import PredictValueMethod
from game.api.predict_val import logging

class AddUser(CreateAPIView):
    serializer_class = AddUsersSerializer
    renderer_classes = [JSONRenderer]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        '''
        Create the users with given username
        '''
        data = {
            'users' : request.data.get('username')
        }
        theme_value = request.data.get('theme_value')

        serializer = AddUsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logging.info('User Added : {}'.format(serializer.data))
            template_name = render_to_string('game/theme/{}/game_card.html'.format(theme_value))
            return Response({ 'data' : serializer.data, 'status_code' : status.HTTP_201_CREATED, 'status' : True , 'template': template_name, 'theme': theme_value})
        return Response(data={ 'errors' : serializer.errors, 'status_code' : status.HTTP_400_BAD_REQUEST,'status' : False })


class PredictValueView(CreateAPIView):
    renderer_classes = [ JSONRenderer ]
    serializer_class = PlayGameSerializer
    def post(self, request, *args, **kwargs):
        '''
        Post the value choosen by user to the api.
        '''
        
        predict_val = random.randint(1,3)
        data = {
            'user_value' : request.data.get('user_value')
        }
        serializer = PlayGameSerializer(data=data)
        if serializer.is_valid():
            pv = PredictValueMethod(int(data['user_value']), predict_val)
            final = pv.find_score()
            return Response(data={'predicted_data':final, 'status_code' : status.HTTP_200_OK , 'status' : True ,'serialize_data': serializer.data })
        return Response(data={ 'errors' : serializer.errors, 'status_code' : status.HTTP_400_BAD_REQUEST,'status' : False })

class FinalResultView(CreateAPIView):
    renderer_classes = [ JSONRenderer ]
    serializer_class = FinalResultSerializer

    def post(self, request, *args, **kwargs):
        '''
        Post the value choosen by user to the api.
        '''
        data = {
            'your_score' : request.data.get('your_score'),
            'com_score' : request.data.get('com_score'),
        }

        serializer = FinalResultSerializer(data=data)
        if serializer.is_valid():
            pv = PredictValueMethod(int(data['your_score']),int(data['com_score']))
            result = pv.final_result()
            return Response(data={'msg':result['msg'],'status_code' : status.HTTP_200_OK , 'status' : True, 'serialize_data':serializer.data, 'result': result['user_won'] })
        return Response(data={ 'errors' : serializer.errors, 'status_code' : status.HTTP_400_BAD_REQUEST,'status' : False })
