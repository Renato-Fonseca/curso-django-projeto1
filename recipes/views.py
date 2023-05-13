from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe, Category


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
         'recipes': recipes,
         'is_detail_page': False,
     })


def recipe(request, id):
    recipes = Recipe.objects.all()
    recipe = recipes[id-1]
    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe': recipe,
        'is_detail_page': True
        })


def category(request, category_id):
    recipes = Recipe.objects.all().order_by('-id')
    related = recipes.filter(category__id=category_id)
    #return render(request, 'recipes/pages/category-view.html', {
     #   'category': category
      #  })

    return render(request, 'recipes/pages/category-view.html', context={
         'recipes': related,
         'is_detail_page': False,
         'category_id': category_id
     })
