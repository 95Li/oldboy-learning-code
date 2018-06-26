from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('APP02---index')


def test(request):
    return HttpResponse('APP02---test')
