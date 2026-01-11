from models import Ingredient, IngredientSource, IngredientType, Meal

from food_list import pantry
from typing import  List
import random


# 1. Generar las bases


def pick_bases(pantry):

  week_bases = []
  for food in pantry:
    if IngredientType.BASE in food.type and food.is_batch:
      week_bases.append(food)

  # All bases appended, should pick 3 of them, or n
  # After, should pick 2 cooked bases and 1 instant base
  return week_bases


protein_food = []


# 0. Store data
for food in pantry:
  if (IngredientSource.PROTEIN == food.source):
    protein_food.append(food)


# 1. Base gen
week_bases = pick_bases(pantry)

for base in week_bases:
    print(f"- {base.name} ({base.kcal} kcal)")


# 2. Generate Meals per base

meals_lunch = []
for  base in week_bases:
  protein = random.choice(protein_food)
  simple_meal = Meal(
    name=f"Food with {base.name}",
    base=base,
    protein=protein,
    carbs_percent=0,
    protein_percent=0,
    fat_percent=0,
    kcal=0
  )
  meals_lunch.append(simple_meal)

print(f"¡He cocinado {len(meals_lunch)} comidas!")
for meal in meals_lunch:
    print(f"--> {meal.name} ({meal.total_kcal()} kcal)")

# idea base:
# Seleccion de bases
# Selecciono 5 veggies
# Selecciono 3 proteins
# Creo las combinaciones
# Las coloco en weekly-planner

