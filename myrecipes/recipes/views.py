from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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


class RecipeCreate(LoginRequiredMixin, generic.CreateView):
    model = Recipe
    # Al insertar redirecciona a la misma url de insercion
    # se usa reverse_lazy xq en este punto la URL no ha sido
    # cargada cuando se importa el fichero
    success_url = reverse_lazy('recipes:new')
    # Campos a mostrar en el formulario,
    # si no se especifica muestra todos
    fields = ['title', 'short_description']

    def form_valid(self, form):
        # Al hacer la validacion, debemos agregar a la receta
        # el autor de esta. Django nos devuelve el usuario
        # mediante el objeto request. Debemos estar logeados
        # para que funcione adecuadamente.
        # Docu: https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/#model-forms
        # En la segunda nota se aclara
        form.instance.author = self.request.user
        redirect_url = super(RecipeCreate, self).form_valid(form)
        # messages.success(self.request, 'Creada receta. La receta está desactivada hasta que un administrador lo revise. ')
        return redirect_url
