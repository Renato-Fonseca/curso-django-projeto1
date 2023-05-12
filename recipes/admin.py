from django.contrib import admin
from recipes.models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    pass



@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

# entenda melhor o decorator e porque ele só funciona atrás do RecipeAdmin
# vídeo explicando decorators: https://www.google.com/search?client=opera&q=how+the+decorators+work+in+Python&sourceid=opera&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:595d0153,vid:nVdF7QT-Ggg 