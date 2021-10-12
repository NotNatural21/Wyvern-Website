from django.shortcuts import render
from . import functions


# Create your views here.
def home(request):
    return render(request, 'CookieBook/home.html')

def cooking(request):
    return render(request, 'CookieBook/cooking.html')


recipe_cooking_list = functions.get_recipe_dict_cooking()

def cookingRecipe(request, recipename):
    recipe = None
    for pair in recipe_cooking_list:
        if pair['url'] == str(recipename):
            recipe = pair
    context = {'recipe': recipe}
    return render(request, 'CookieBook/recipe.html', context)
    
def baking(request):
    return render(request, 'CookieBook/baking.html')