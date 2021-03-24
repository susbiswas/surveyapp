from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse, JsonResponse
from users.models import CustomUser
from django.shortcuts import render


def surveyapp(request):
    return render(request, 'line_chart.html')

def chart(request):
    data = []
    count= CustomUser.objects.count()
    male_count = CustomUser.objects.filter(sex = 'M').count()
    female_count = CustomUser.objects.filter(sex = 'F').count()
    other_count = CustomUser.objects.filter(sex = 'O').count()
    data.append(male_count)
    data.append(female_count)
    data.append(other_count)
    labels = ['Male','Female','Others']

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def get_labels(count):
    labels = []
    for i in range(1, 6):
        rem = count % 10
        count = count/10    
        if(count != 0):
            labels.append(count)
            continue
        else:
            labels.append(rem)
    return labels

