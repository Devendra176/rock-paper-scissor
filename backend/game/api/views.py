from rest_framework.renderers import JSONRenderer
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from .serializers import (AddUsersSerializer, PlayGameSerializer, FinalResultSerializer)
from .predict_val import PredictValueMethod
import random

from .predict_val import logging

class AddUser(CreateAPIView):
    serializer_class = AddUsersSerializer
    renderer_classes = [ JSONRenderer ]

    def post(self, request, *args, **kwargs):
        '''
        Create the users with given username
        '''
        data = {
            'users' : request.data.get('username')
        }

        serializer = AddUsersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            logging.info('User Added : {}'.format(serializer.data))
            return Response(data={ 'data' : serializer.data, 'status_code' : status.HTTP_201_CREATED, 'status' : True })
        return Response(data={ 'errors' : serializer.errors, 'status_code' : status.HTTP_400_BAD_REQUEST,'status' : False })


class PredictValueView(CreateAPIView):
    renderer_classes = [ JSONRenderer ]
    serializer_class = PlayGameSerializer
    def post(self, request, *args, **kwargs):
        '''
        Post the value choosen by user to the api.
        '''
        
        predict_val = random.randint(1,3)
        user_value = request.data.get('user_value')
        pv = PredictValueMethod(int(user_value), predict_val)
        final = pv.find_score()
        return Response(data={'predicted_data':final, 'status_code' : status.HTTP_200_OK , 'status' : True })

class FinalResultView(CreateAPIView):
    renderer_classes = [ JSONRenderer ]
    serializer_class = FinalResultSerializer

    def post(self, request, *args, **kwargs):
        '''
        Post the value choosen by user to the api.
        '''
        your_score = request.data.get('your_score')
        com_score = request.data.get('com_score')
        pv = PredictValueMethod(int(your_score),int(com_score))
        result = pv.final_result()
        return Response(data={'msg':result['msg'],'status_code' : status.HTTP_200_OK , 'status' : True })
