from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# HTTP REQUEST
def home(request):
    return HttpResponse('Home')
    # return HTTP response

# HTTP REQUEST


def sobre(request):
    return HttpResponse('Sobre')
    # return HTTP response

# HTTP REQUEST


def contato(request):
    return HttpResponse('Contato')
    # return HTTP response
