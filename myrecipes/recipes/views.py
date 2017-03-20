from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import View


from .models import Recipe


class Index(generic.ListView):
    """
    Recipe list
    """
    template_name = 'recipes/index.html'
    context_object_name = 'latest_recipes_list'
    paginate_by = 5

    def get_queryset(self):
        """
        Return the last five published recipes (not including those set to be
        published in the future).
        """
        return Recipe.objects.order_by('datetime_modificated')
        # return Recipe.objects.values_list('id', 'title').order_by('datetime_modificated')[:5]


class Detail(generic.DetailView):
    """
    Recipe info
    """
    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipe.objects.all()

    # def get_context_data(self, **kwargs):
    #     """
    #     Excludes any recipes that aren't published yet.
    #     """
    #     context = super(Detail, self).get_context_data(**kwargs)


def new_recipe(request):
    """
    New recipe form
    """
    return render(request, 'recipes/base.html')


class CreateRecipe(generic.CreateView):
    model = Recipe
    # form_class = UserForm
    success_url = reverse_lazy('recipes:new')
    fields = ['title', 'short_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        redirect_url = super(CreateRecipe, self).form_valid(form)
        # messages.success(self.request, 'Creada receta. La receta está desactivada hasta que un administrador lo revise. ')
        return redirect_url
