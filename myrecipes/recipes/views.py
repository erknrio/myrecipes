from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import Recipes


class Index(generic.ListView):
    """
    Recipes list
    """
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipes_list'

    def get_queryset(self):
        """
        Return the last five published recipes (not including those set to be
        published in the future).
        """
        return Recipes.objects.order_by('title')[:5]


class Detail(generic.DetailView):
    """
    Recipe info
    """
    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipes.objects.all()

    # def get_context_data(self, **kwargs):
    #     """
    #     Excludes any recipes that aren't published yet.
    #     """
    #     context = super(Detail, self).get_context_data(**kwargs)


def new_recipe(request):
    """
    New recipe form
    """
    return render(request, 'recipes/new.html')


def create_recipe(request, recipe_id):
    """
    Save recipe to database
    """
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    print(recipe)
    print(request.POST)
    # return HttpResponseRedirect(reverse('recipes:results', args=(recipe.id)))
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         # form = RecipeName(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         # form = RecipeName()
#
#     return render(request, 'index.html', {'form': form})
