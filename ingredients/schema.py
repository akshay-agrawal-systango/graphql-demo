import graphene
from graphene import relay
from ingredients.models import Category, Ingredient
from ingredients.types import IngredientType, CategoryType
from .mutations import CreateIngredientMutation, EditIngredientMutation
from graphene_django.filter import DjangoFilterConnectionField


class Query(graphene.ObjectType):
    # all_ingredients = graphene.List(IngredientType)
    # all_categories = graphene.List(CategoryType)
    category = relay.Node.Field(CategoryType)
    all_categories = DjangoFilterConnectionField(CategoryType)
    ingredient = relay.Node.Field(IngredientType)
    all_ingredients = DjangoFilterConnectionField(IngredientType)

    ingredient_by_name = graphene.Field(IngredientType, name=graphene.String(required=True))
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_ingredient_by_name(root, info, name):
        try:
            return Ingredient.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredientMutation.Field()
    edit_ingredient = EditIngredientMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)