import random

good_guy = {
    "Health": 1000,
    "Name": "Hercules",
    "MainAttack": "Punch",
    "AltAttack": "Kick",
    "Punch": 25,
    "Kick": 20
}

# print(good_guy["AltAttack"])
# print(good_guy["Kick"])
lion = {
    "Name": "Nemean Lion",
    "Health": 100,
    "MainAttack": "Scratch",
    "AltAttack": "Bite",
    "Bite": 10,
    "Scratch": 20
}

def attack():
    new_lion_health = lion["Health"] - good_guy["Punch"]
    print(new_lion_health)

attack()
