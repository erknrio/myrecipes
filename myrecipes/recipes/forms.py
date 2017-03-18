from django import forms


class RecipeName(forms.Form):
    recipe_name = forms.CharField(label='Nombre', max_length=50)


class RecipeShortDescription:
    def __init__(self, data_from_post=None):
        print(data_from_post)
        print(data_from_post.get('recipe_name', None))
        # if data_form_post is not None:
        #   _post = data_from_post
        #   name = _post.get('recipe_name', None)
        #   print(name)

        # for carname in list_of_cars:
        #    self.fields['car_%s' % carname] = forms.CharField(label=carname)
