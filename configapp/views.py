from django.http import HttpResponse


def app(request):
    return HttpResponse("1-appning funksiyasi")


def app1(request):
    return HttpResponse("1-appning 2-funksiyasi.")


def app2(request):
    return HttpResponse("1-appning 3-funksiyasi.")
