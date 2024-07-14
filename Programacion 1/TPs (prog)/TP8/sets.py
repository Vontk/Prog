from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    temp_set = set()
    for ingredient in dish_ingredients:
        temp_set.add(ingredient)
    return_tuple = (dish_name, temp_set)
    return return_tuple


def check_drinks(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"
