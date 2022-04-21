#from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# HTTP REQUEST
def home(request):
    # o render entende que esse arquivo pode estar na pasta "templates", basta nao esquecer de adicionar o app criado no settings
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Testing name in context',
    })
