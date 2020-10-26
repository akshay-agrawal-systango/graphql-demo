# from graphene_django import DjangoObjectType
# from .models import Category, Ingredient

# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'


from graphene import relay
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )