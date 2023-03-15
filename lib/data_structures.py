spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [key["name"] for key in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [key for key in spicy_foods if key["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine_type = food["cuisine"]
        heat = food["heat_level"] * "🌶"
        print(f"{name} ({cuisine_type}) | Heat Level: {heat}")
        

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [key for key in spicy_foods if key["cuisine"].lower() == cuisine.lower()][0]
# HOW TO RETURN A SINGLE DICT?????

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine_type = food["cuisine"]
        heat = food["heat_level"] * "🌶"
        if food["heat_level"] > 5:
            print(f"{name} ({cuisine_type}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    heat_levels = [key["heat_level"] for key in spicy_foods]
    return (sum(heat_levels))/(len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
