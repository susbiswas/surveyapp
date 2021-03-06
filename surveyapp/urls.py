"""surveyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chartapp import views
from chartapp.views import ChatterBotApiView,ChatterBotAppView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.surveyapp, name='surveyapp'),
    path('prevaccinechart_gender/', views.prevaccinechart_gender, name='prevaccinechart_gender'),
    path('postvaccinechart_gender/', views.postvaccinechart_gender, name='postvaccinechart_gender'),
    path('prevaccinechart_race/', views.prevaccinechart_race, name='prevaccinechart_race'),
    path('postvaccinechart_race/', views.postvaccinechart_race, name='postvaccinechart_race'),
    path('chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    path('chatbot/', ChatterBotAppView.as_view(), name='main'),
]
