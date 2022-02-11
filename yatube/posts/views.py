from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Добро пожаловать на YAtube')

def group_list(request):
    return HttpResponse('Список сообществ')

def group_posts(request, slug):
    return HttpResponse(f'Сообщества {slug}')
