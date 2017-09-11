from django import forms

from .models import RecipePost

class PostForm(forms.ModelForm):

    class Meta:
        model = RecipePost
        fields = ('title', 'photo', 'prep_time' ,'cooking_time', 'servings', 'ingridients', 'cooking_instaructions', 'published_date') 