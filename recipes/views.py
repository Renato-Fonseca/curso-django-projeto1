from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from utils.recipes.factory import make_recipe

from .models import Category, Recipe


def home(request):
    recipes = Recipe.objects.all().order_by("-id").filter(is_published=True)
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
            "is_detail_page": False,
        },
    )


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True)
    return render(
        request,
        "recipes/pages/recipe-view.html",
        {"recipe": recipe, "is_detail_page": True},
    )


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by(
            "-id"
        )
    )

    return render(
        request,
        "recipes/pages/category-view.html",
        context={
            "recipes": recipes,
            "is_detail_page": False,
            "title": recipes[0].category.name,
        },
    )
