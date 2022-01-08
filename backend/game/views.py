from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class GetFrontPage(APIView):

    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request):
        response = {}
        response['msg'] = 'Hello! welcome to the djnago game'
        return Response(response,template_name='index.html')



    


