from django.shortcuts import render, HttpResponse
from django.urls import reverse


# Create your views here.

def index(request, num):
    # url_name = reverse('app01:app01-index', kwargs={'num': num})
    url_name = reverse('app01:app01-index',args=(num,))
    print(url_name)
    return HttpResponse('APP01----index-------' + num + '---' + url_name)
