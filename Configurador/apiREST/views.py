# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from apiREST.models import *
from apiREST.serializers import *
# Create your views here.

#-------------------------------UTILS-------------------------------

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(JSONResponse, self).__init__(content,**kwargs)

def consoleLog(text='Información',data= ''):
    print('########## {text} : {data} ##########'.format(text=text, data=data))

@csrf_exempt
def data(request):
	characters = Character.objects.all()
	stages = Stage.objects.all()

	serializer_c = CharacterSerializer(characters, many=True)
	serializer_s = StageSerializer(stages, many=True)

	responde = {'characters':serializer_c.data,'scenarios':serializer_s.data}
	return JSONResponse(responde)
