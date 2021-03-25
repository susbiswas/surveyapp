from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from users.models import CustomUser
from django.shortcuts import render


def surveyapp(request):
    return render(request, 'line_chart.html')

def prevaccinechart_gender(request):
    data = []
    count= CustomUser.objects.count()
    male_count = CustomUser.objects.filter(sex = 'M').count()
    female_count = CustomUser.objects.filter(sex = 'F').count()
    other_count = CustomUser.objects.filter(sex = 'O').count()
    data.append(male_count)
    data.append(female_count)
    data.append(other_count)
    labels = get_gender_labels()

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def postvaccinechart_gender(request):
    data = []
    count= CustomUser.objects.count()
    male_count = CustomUser.objects.filter(sex = 'M').count()
    female_count = CustomUser.objects.filter(sex = 'F').count()
    other_count = CustomUser.objects.filter(sex = 'O').count()
    data.append(male_count)
    data.append(female_count)
    data.append(other_count)
    labels = get_gender_labels()

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def prevaccinechart_race(request):
    data = []
    count= CustomUser.objects.count()
    male_count = CustomUser.objects.filter(sex = 'M').count()
    female_count = CustomUser.objects.filter(sex = 'F').count()
    other_count = CustomUser.objects.filter(sex = 'O').count()
    data.append(male_count)
    data.append(female_count)
    data.append(other_count)
    labels = get_race_labels()

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def postvaccinechart_race(request):
    data = []
    count= CustomUser.objects.count()
    male_count = CustomUser.objects.filter(sex = 'M').count()
    female_count = CustomUser.objects.filter(sex = 'F').count()
    other_count = CustomUser.objects.filter(sex = 'O').count()
    data.append(male_count)
    data.append(female_count)
    data.append(other_count)
    labels = get_race_labels()

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def get_gender_labels():
    return ['Male','Female','Others']

def get_race_labels():
    return ['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latin','Native Hawaiian or Other Pacific Islander','White']