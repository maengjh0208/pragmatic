from django.http import HttpResponse


def hello_word(request):
    return HttpResponse('hello world')
