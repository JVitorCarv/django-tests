from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe


# Create your views here.
# HTTP REQUEST
def home(request):
    # o render entende que esse arquivo pode estar na pasta "templates", basta nao esquecer de adicionar o app criado no settings
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
    })
