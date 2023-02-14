from django.http import HttpResponse


def coffee(request):
    return HttpResponse("<body> Я чайник </body>", status=418)
