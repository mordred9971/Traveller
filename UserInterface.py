import Character
import Util
from Util import Roll

char = Character.Character();


def Begin():
    char.name = input("WELCOME NEW UNIDENTIFIED TRAVELLER. ENTER YOUR NAME HERE AND WE SHALL BEGIN: ")
    print("THANK YOU", char.name)
    char.species = input("PLEASE ENTER YOUR RACE HERE: ")
    print("THANK YOU VALUED CITIZEN. WE WILL NOW GENERATE YOUR PHYSICAL AND MENTAL FORM")
    stats = Roll(2, 6, 0)
    print("THESE ARE YOUR COMPANY DERIVED STATS:", stats)
    for stat in char.stats:
        if stat != "PSI":
            char.stats[stat] = int(input("ENTER A STAT FOR {}: ".format(stat)))
    print("IT IS NOW TIME FOR YOU TO CHOOSE YOUR BACKGROUND SKILLS")
    for x in range(1, 3 + Util.mod(char.stats['Education'])):
        char.skills[input("Enter your Chosen Skill: ")] = '0'


Begin()
