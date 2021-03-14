from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_data(request, *args, **kwargs):
    labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = [10, 23, 2, 3, 12, 2]
    data = {
            "labels": labels,
            "default": default_items,
    }
    return JsonResponse(data)
