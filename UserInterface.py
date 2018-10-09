import random

import Character

char = Character.Character();


def Begin():
    char.name = input("WELCOME NEW UNIDENTIFIED TRAVELLER. ENTER YOUR NAME HERE AND WE SHALL BEGIN: ")
    print("THANK YOU", char.name)
    char.species = input("PLEASE ENTER YOUR RACE HERE: ")
    print("THANK YOU VALUED CITIZEN. WE WILL NOW GENERATE YOUR PHYSICAL AND MENTAL FORM")
    stats = Roll(2, 6, 0)
    print("THESE ARE YOUR COMPANY DERIVED STATS:", stats)
    for stat in char.stats:
        if stat != "Psy":
            char.stats[stat] = int(input("ENTER A STAT FOR {}".format(stat)))


def Roll(num, repeat, mod):
    result = []
    for i in range(repeat):
        hold = 0
        for n in range(num):
            hold += random.randint(1, 6)
        hold += mod
        result.append(hold)
    return result


Begin()
