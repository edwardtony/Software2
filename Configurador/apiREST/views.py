# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.parsers import JSONParser
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
def scenarios(request):
	# stages =  [state.as_dict() for state in Stage.objects.all().order_by('order')]
	stages =  [state.as_dict() for state in Stage.objects.all().filter(order__in=[1])]
	return JSONResponse(stages)

@csrf_exempt
def characters(request):
	characters = [character.as_dict() for character in Character.objects.all()]
	return JSONResponse(characters)


#-------------------------------PLAYER-------------------------------

@csrf_exempt
def player_list(request):
    """
    List all code player_list, or create a new player_list.
    """
    rows = request.GET.get('rows',10)
    if request.method == 'GET':
        players = [player.as_dict() for player in Player.objects.all().order_by('-score')[0:int(rows)]]
        return JSONResponse(players)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            job_request = JobRequest.objects.get(pk = serializer.data['id'])
            return JSONResponse(data, status=201)
        print(serializer.errors)
        return JSONResponse(serializer.errors, status=400)
    else:
        return HttpResponse(405)
