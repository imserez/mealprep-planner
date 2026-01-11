from models import Ingredient, IngredientType, IngredientSource

# Creamos una LISTA de ingredientes (tu despensa)
pantry = [
    Ingredient(
        id=1, name="Patata", type=[IngredientType.BASE],
        kcal=70, carbs=15.71, protein=1.68, fat=0.1
    ),
    Ingredient(
        id=2, name="Pepino", type=[IngredientType.COMPLEMENT],
        kcal=12, carbs=2.16, protein=0.59, fat=0.16
    ),
    Ingredient(
        id=3, name="Salmón", type=[IngredientType.BASE],
        kcal=146, carbs=0, protein=21.62, fat=5.93
    ),
    Ingredient(
        id=4, name="Yogur natural 0% Hacendado", type=[IngredientType.EXTRA],
        kcal=45, carbs=5.62, protein=5.38, fat=0.1
    ),
    Ingredient(
        id=5, name="Chía", type=[IngredientType.EXTRA],
        kcal=464, carbs=42.6, protein=22, fat=34
    ),
    Ingredient(
        id=6, name="Tomate cherry", type=[IngredientType.COMPLEMENT],
        kcal=18, carbs=3.9, protein=0.88, fat=0.2
    ),
    Ingredient(
        id=7, name="Arroz Integral", type=[IngredientType.BASE],
        kcal=350, carbs=72, protein=7.6, fat=2.8, is_batch=True
    ),
    Ingredient(
        id=8, name="Champiñones", type=[IngredientType.COMPLEMENT],
        kcal=22, carbs=3.28, protein=3.09, fat=0.34
    ),
    Ingredient(
        id=9, name="Brócoli", type=[IngredientType.COMPLEMENT],
        kcal=34, carbs=6.64, protein=2.82, fat=0.37
    ),
    Ingredient(
        id=10, name="Pimiento rojo", type=[IngredientType.COMPLEMENT],
        kcal=28, carbs=4.5, protein=0.9, fat=0.5
    ),
    Ingredient(
        id=11, name="Huevo", type=[IngredientType.BASE],
        kcal=74, carbs=0.38, protein=6.29, fat=4.97
    ),
    Ingredient(
        id=12, name="Maíz dulce", type=[IngredientType.COMPLEMENT],
        kcal=75, carbs=9.32, protein=2.6, fat=2.3
    ),
    Ingredient(
        id=13, name="Lentejas", type=[IngredientType.BASE],
        kcal=353, carbs=60.08, protein=25.81, fat=1.06, is_batch=True
    ),
    Ingredient(
        id=14, name="Pechuga de pollo", type=[IngredientType.BASE],
        kcal=195, carbs=0, protein=29.55, fat=7.72
    ),
    Ingredient(
        id=15, name="Calabacín", type=[IngredientType.COMPLEMENT],
        kcal=16, carbs=3.35, protein=1.21, fat=0.18
    ),
    Ingredient(
        id=16, name="Pasta con vegetales", type=[IngredientType.BASE],
        kcal=352, carbs=72, protein=13, fat=1.5
    ),
    Ingredient(
        id=17, name="Tomate frito bote", type=[IngredientType.EXTRA],
        kcal=162, carbs=23.2, protein=2.86, fat=6.5 # Estimado grasa
    ),
    Ingredient(
        id=18, name="Espárrago", type=[IngredientType.COMPLEMENT],
        kcal=20, carbs=3.88, protein=2.2, fat=0.12
    ),
    # Nota: Los datos de la salsa gatito eran confusos, he puesto una estimación estándar
    Ingredient(
        id=19, name="Salsa de pimiento", type=[IngredientType.EXTRA],
        kcal=237, carbs=32, protein=3.7, fat=12
    ),
    Ingredient(
        id=20, name="Ajo", type=[IngredientType.EXTRA],
        kcal=40, carbs=9.9, protein=1.9, fat=0.02
    ),
    Ingredient(
        id=21, name="Cebolla", type=[IngredientType.COMPLEMENT],
        kcal=42, carbs=10.1, protein=0.92, fat=0.08
    ),
    Ingredient(
        id=22, name="Perejil", type=[IngredientType.EXTRA],
        kcal=36, carbs=6.33, protein=2.97, fat=0.79
    ),
    Ingredient(
        id=23, name="Leche semi", type=[IngredientType.EXTRA],
        kcal=115, carbs=12, protein=7.84, fat=4.0 # Estimado grasa
    ),
    Ingredient(
        id=24, name="Queso parmesano", type=[IngredientType.EXTRA],
        kcal=392, carbs=3.22, protein=35.75, fat=25.83
    ),
    Ingredient(
        id=25, name="Garbanzos", type=[IngredientType.BASE],
        kcal=180, carbs=29.98, protein=9.54, fat=2.99, is_batch=True
    ),
    Ingredient(
        id=26, name="Carne picada mix", type=[IngredientType.BASE],
        kcal=195, carbs=2, protein=17, fat=12
    ),
    Ingredient(
        id=27, name="Berenjena entera (550g)", type=[IngredientType.BASE],
        kcal=132, carbs=31.2, protein=5.53, fat=1.04
    ),
    Ingredient(
        id=28, name="Manzana", type=[IngredientType.COMPLEMENT],
        kcal=72, carbs=19.06, protein=0.36, fat=0.23
    ),
    Ingredient(
        id=29, name="Plátano", type=[IngredientType.COMPLEMENT],
        kcal=105, carbs=26.95, protein=1.29, fat=0.39
    ),
    Ingredient(
        id=30, name="Salteado Mercadona", type=[IngredientType.COMPLEMENT],
        kcal=30, carbs=3.8, protein=2, fat=0.3
    ),
    Ingredient(
        id=31, name="Avena", type=[IngredientType.BASE],
        kcal=389, carbs=66.27, protein=16.89, fat=6.9
    ),
    Ingredient(
        id=32, name="Nueces", type=[IngredientType.EXTRA],
        kcal=654, carbs=13.71, protein=15.23, fat=65.21
    ),
    Ingredient(
        id=33, name="Arándanos", type=[IngredientType.COMPLEMENT],
        kcal=52, carbs=11, protein=0.7, fat=0.1
    ),
    Ingredient(
        id=34, name="Rebanada pan integral", type=[IngredientType.BASE],
        kcal=69, carbs=11.3, protein=3.0, fat=0.9
    ),
    Ingredient(
        id=35, name="Loncha de pavo", type=[IngredientType.COMPLEMENT],
        kcal=80, carbs=1.3, protein=17.9, fat=0.08
    ),
    Ingredient(
        id=36, name="Queso havarti light (loncha)", type=[IngredientType.COMPLEMENT],
        kcal=67, carbs=0.5, protein=6.8, fat=4.3
    ),
    Ingredient(
        id=37, name="Queso fresco batido (tarrina)", type=[IngredientType.BASE],
        kcal=230, carbs=17.5, protein=40, fat=0.1
    ),
    Ingredient(
        id=38, name="Proteína vainilla", type=[IngredientType.COMPLEMENT],
        kcal=114, carbs=2.7, protein=21.8, fat=1.8
    ),
    Ingredient(
        id=39, name="Lata atún natural", type=[IngredientType.COMPLEMENT],
        kcal=58, carbs=0.5, protein=12.6, fat=0.72
    ),
    Ingredient(
        id=40, name="Crema calabacín (350g)", type=[IngredientType.BASE],
        kcal=126, carbs=19.25, protein=1.05, fat=3.5
    ),
    Ingredient(
        id=41, name="Penne rigate integral", type=[IngredientType.BASE],
        kcal=347, carbs=67, protein=12, fat=1.9
    ),
    Ingredient(
        id=42, name="Brotes tiernos", type=[IngredientType.COMPLEMENT],
        kcal=22, carbs=1.5, protein=1.6, fat=0.6
    ),
    Ingredient(
        id=43, name="Espinaca picada", type=[IngredientType.COMPLEMENT],
        kcal=27, carbs=1.5, protein=2.9, fat=0.4
    ),
    Ingredient(
        id=44, name="Sofrito Mercadona", type=[IngredientType.EXTRA],
        kcal=30, carbs=5.2, protein=1.4, fat=0.2
    ),
    Ingredient(
        id=45, name="Pimiento congelado", type=[IngredientType.COMPLEMENT],
        kcal=28, carbs=4.5, protein=0.9, fat=0.5
    ),
    Ingredient(
        id=46, name="Espárrago verde congelado", type=[IngredientType.COMPLEMENT],
        kcal=28, carbs=2.9, protein=2.6, fat=0.6
    ),
    Ingredient(
        id=47, name="Edamame", type=[IngredientType.COMPLEMENT],
        kcal=130, carbs=10, protein=11, fat=4
    ),
]

print(f"Loaded {len(pantry)} ingredients!")

print("\n--- High-Protein food ---")
for ing in pantry:
    if ing.source == IngredientSource.PROTEIN:
        print(f"🍗 {ing.name} ({ing.kcal} kcal)")