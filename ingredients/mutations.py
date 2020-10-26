import graphene
from .models import Ingredient
from django import forms
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation, DjangoFormMutation


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class EditIngredientMutation(DjangoModelFormMutation):

    class Meta:
        form_class = IngredientForm


class CreateIngredientMutation(DjangoFormMutation):
    class Meta:
        form_class = IngredientForm