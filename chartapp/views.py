from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from users.models import CustomUser
from django.shortcuts import render
from django.db import connection


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
    print(data)
    return JsonResponse(data={
        'labels': labels,
        'defaultdata': data,
    })

def get_gender_labels():
    return ['Male','Female','Others']

def get_race_labels():
    return ['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latin','Native Hawaiian or Other Pacific Islander','White']