from models import Ingredient, IngredientSource, IngredientType



potato = Ingredient (
  id = 1,
  type = [IngredientType.COMPLEMENT, IngredientType.BASE],
  name = "Potato",
  kcal = 70,
  carbs = 15.71,
  protein = 1.68,
  fat = 0.1,
  source = None
)

print(potato.model_dump_json(indent = 2))