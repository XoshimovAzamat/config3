from django.http import HttpResponse


def app3(request):
    return HttpResponse("2-appning 1-funksiyasi")


def app4(request):
    return HttpResponse("2-appning 2-funksiyasi.")


def app5(request):
    return HttpResponse("2-appning 3-funksiyasi.")
