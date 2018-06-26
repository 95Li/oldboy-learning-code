from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        if request.POST.get('name') == 'lyj' and request.POST.get('pwd') == '123':

            request.session['login'] = 'ok'
            request.session.set_expiry(3)
            request.session.clear_expired()
            return redirect('/home/')

        else:
            return render(request, 'login.html')


def home(request):
    return HttpResponse('This is HOME Page')
