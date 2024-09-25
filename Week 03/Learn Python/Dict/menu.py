# observe the dictionary above and write a menu driven python program to create recipes. Once one recipe is done then the quantity of the items in pantry should also be reduced
# Eg  :  If you cook beans on toast the beans quantity and bread quantity need to decrease i.e., one from the total quantity each.
pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}
recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}

def cook(items):
    for itm in items:
        if itm in pantry and pantry[itm] != 0:
            pantry[itm] -= 1
        else:
            return False
    return True

item = input("Enter your item you want: ")
if item in recipes:
    items = recipes[item]
    ready = cook(items)
    if ready:
        print("Your item Ready")
    else:
        print("Recipie not available!")
else:
    print("Your item is not available")