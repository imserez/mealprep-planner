from pydantic import BaseModel, PositiveFloat, model_validator
from enum import Enum
from typing import Optional, List

class IngredientType(str, Enum):
  BASE = "base"
  COMPLEMENT = "complement"
  EXTRA = "extra"

class IngredientSource(str, Enum):
  CARB = "carb"
  PROTEIN = "protein"
  FAT = "fat"
  SEASONING = "seasoning"
  VEGGIE = "veggie"


class Ingredient(BaseModel):
  id: int
  name: str
  kcal: float
  type: List[IngredientType]
  # type: IngredientType | None = None
  kcal: float
  carbs: float
  protein: float
  fat: float
  source: Optional[IngredientSource] = None
  is_batch: bool | bool = False


  @model_validator(mode = 'after')
  def calculate_source(self):
    if self.source is not None:
      return self;

    if self.kcal < 50:
      self.source = IngredientSource.VEGGIE
    if self.carbs > self.protein and self.carbs > self.fat:
      self.source = IngredientSource.CARB
    elif self.protein > self.carbs:
      self.source = IngredientSource.PROTEIN
    else:
      self.source = IngredientSource.FAT

    return self


# class MealType(str, Enum):
#   LUNCH = "lunch"
#   DINNER = "dinner"

class Meal(BaseModel):
  name: str
  base: Ingredient | None
  protein: Ingredient | None
  veggie: Ingredient | None
  accesory: Ingredient | None
  carbs_percent: int
  protein_percent: int
  fat_percent: int
  kcal: int
  # type: MealType
