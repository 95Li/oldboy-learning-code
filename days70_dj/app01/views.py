from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django import views
from app01 import models

from functools import wraps


def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.get_signed_cookie('login', salt='aaa', default=None) == 'ok':
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return inner


# def book_list(request):
#     cookie = request.get_signed_cookie('login', salt='aaa',default=None)
#     print(cookie)
#     if cookie == 'ok':
#         data = models.Book.objects.all()
#         return render(request, 'book_list.html', {'book_list': data})
#     else:
#         return redirect('/login/')

@login_check
def book_list(request):
    data = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_list': data})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user_info = models.User.objects.filter(name=name, pwd=pwd)
        if user_info:
            response = redirect('/book_list/')
            response.set_signed_cookie('login', 'ok', salt='aaa')
            return response
        else:
            render(request, 'login.html')


class Books(views.View):
    def get(self, request):
        pass

    def post(self):
        pass
