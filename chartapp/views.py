from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from users.models import CustomUser
from django.shortcuts import render
from django.db import connection
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings


def surveyapp(request):
    return render(request, 'line_chart.html')

def prevaccinechart_gender(request):
    data = []
    labels = get_gender_labels()
    parameter = ['M','F','O']
    for i in parameter:
        params = {'sex':i}
        sql_stmt = '''
             Select count(*) FROM Customer c JOIN chartapp_prevaccine_health_issue p on c.cid = p.cid where c.sex =:sex
        '''
        with connection.cursor() as cursor:
            cursor.execute(sql_stmt, params)
            row = cursor.fetchone()
            data.append(row[0])
    
    return JsonResponse(data={
        'labels': labels,
        'defaultdata': data,
    })

def postvaccinechart_gender(request):
    data = []
    labels = get_gender_labels()
    parameter = ['M','F','O']
    for i in parameter:
        params = {'sex':i}
        sql_stmt = '''
            Select count(*) FROM Customer c JOIN chartapp_postvaccine_health_issue p on c.cid = p.cid where c.sex =:sex
        '''
        with connection.cursor() as cursor:
                cursor.execute(sql_stmt, params)
                row = cursor.fetchone()
                data.append(row[0])

    return JsonResponse(data={
        'labels': labels,
        'defaultdata': data,
    })

def prevaccinechart_race(request):
    data = []
    labels = get_race_labels()
    
    for i in labels:
        params = {'race':i}
        sql_stmt = '''
            Select count(*) FROM Customer c JOIN chartapp_prevaccine_health_issue p on c.cid = p.cid where c.race =:race
        '''
        with connection.cursor() as cursor:
                cursor.execute(sql_stmt, params)
                row = cursor.fetchone()
                data.append(row[0])
        

    return JsonResponse(data={
        'labels': labels,
        'defaultdata': data,
    })
    

def postvaccinechart_race(request):
    data = []
    labels = get_race_labels()
    for i in labels:
        params = {'race':i}
        sql_stmt = '''
            Select count(*) FROM Customer c JOIN chartapp_postvaccine_health_issue p on c.cid = p.cid where c.race =:race
        '''
        with connection.cursor() as cursor:
                cursor.execute(sql_stmt, params)
                row = cursor.fetchone()
                data.append(row[0])
    return JsonResponse(data={
        'labels': labels,
        'defaultdata': data,
    })

def get_gender_labels():
    return ['Male','Female','Others']

def get_race_labels():
    return ['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latin','Native Hawaiian or Other Pacific Islander','White']

class ChatterBotAppView(TemplateView):
    template_name = 'chatbot.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })