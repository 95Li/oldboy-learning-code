from django.shortcuts import render, HttpResponse


# Create your views here.

def ajax_test(request):
    if request.method == 'POST':
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')

        print(i2)
        res = int(i1) + int(i2[0])
        return HttpResponse(res)
    return render(request, 'ajax_text.html')


def upload(request):
    file = request.FILES.get('f1')
    print(file)
    return HttpResponse('upload')
