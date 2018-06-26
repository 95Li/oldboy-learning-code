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
            return redirect('/cbv_login/')

    return inner


from django.utils.decorators import method_decorator


class Book_view(views.View):

    @method_decorator(login_check)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = models.Book.objects.all()
        return render(request, 'book_list.html', {'book_list': data})

    def post(self, request):
        data = models.Book.objects.all()
        return render(request, 'book_list.html', {'book_list': data})


class Login_view(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user_info = models.User.objects.filter(name=name, pwd=pwd)
        if user_info:
            request.session['login'] = 'ok'
            request.session['user'] = name
            return redirect('/cbv_book_list/')
