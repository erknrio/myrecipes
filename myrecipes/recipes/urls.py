from django.conf.urls import url

from . import views

# Namspace: https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names
app_name = 'recipes'
# Url list
urlpatterns = [
    # ex: /recipes/
    url(r'^$', views.Index.as_view(), name='index'),
    # ex: /recipes/1/
    url(r'^(?P<pk>[0-9]+)/$', views.Detail.as_view(), name='detail'),
    # ex: /recipes/new/
    url(r'^new/$', views.new_recipe, name='new'),
    # ex: /recipes/create
    url(r'^create/$', views.create_recipe, name='create'),
]
