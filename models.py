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

  @model_validator(mode = 'after')
  def calculate_source(self):
    if self.source is not None:
      return self;

    if self.carbs > self.protein and self.carbs > self.fat:
      self.source = IngredientSource.CARB
    elif self.protein > self.carbs:
      self.source = IngredientSource.PROTEIN
    else:
      self.source = IngredientSource.FAT

    return self


