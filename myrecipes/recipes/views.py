from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RecipeName, RecipeShortDescription


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecipeName(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeName()

    return render(request, 'myform_1_template.html', {'form': form})


def list_cars_for_brand_view(request):
    form = RecipeShortDescription()
    return render(request, 'myform_2_template.html', {'form': form})
