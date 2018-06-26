from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django import views
from app01 import models

from functools import wraps


def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if request.session.get('login') == 'ok':
            return func(request, *args, **kwargs)
        else:
            return redirect('/se_login/')

    return inner


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
            # 登陆成功
            # 1. 生成随机字符串（口令），给浏览器返回
            # 2. 在服务端开辟一块空间，用来保存对应的session数据（大字典）
            # 3. 在服务端开辟的空间中保存需要保存的键值对数据
            request.session['login'] = 'ok'
            request.session['user'] = name

            return redirect('/se_book_list/')
        else:
            render(request, 'login.html')
