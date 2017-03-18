from django.conf.urls import url

from . import views
from .forms import RecipeName, RecipeShortDescription

# Namspace: https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names
app_name = 'polls'
# Url list
urlpatterns = [
    # ex: /polls/
    url(r'^$', WizardForm.as_view([RecipeName, RecipeShortDescription])
]
