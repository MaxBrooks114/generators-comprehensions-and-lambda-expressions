menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)

# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in
# meal]
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]

print(meals)


fuss_meals = [meal for meal in menu if "spam" or 'eggs' in meal if not (
    "bacon" in meal and "sausage" in meal)]

print(fuss_meals)


fuss_meals = [meal for meal in menu if ("spam" in meal or 'eggs' in meal) and
              not (
        "bacon" in meal and "sausage" in meal)]

print(fuss_meals)
