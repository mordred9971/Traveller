from enum import Enum


class Attributes(Enum):
    STRENGTH = "Strength"
    ENDURANCE = "Endurance"
    DEXTERITY = "Dexterity"
    INTELLIGENCE = "Intelligence"
    EDUCATION = "Education"
    PSI = "PSI"


class SKILLS(Enum):
    ADMIN = "Admin"
    ADVOCATE = "Advocate"
    ANIMALS_HANDLING = "Animals(Handling)"
    ANIMALS_TRAINING = "Animals(Training)"
    ANIMALS_VETERINARY = "Animals(Veterinary)"
    ATHELETICS_DEX = "Athletics(Dex)"
    ATHELETICS_END = "Athletics(End)"
    ATHELETICS_STR = "Athletics(Stronk)"
    ART = "ART"
    ASTROGATION = "Astrogration"
    BROKER = "Broker"
    CAROUSE = "Carouse"
    DECEPTION = "Deception"
    DIPLOMAT = "Diplomat"
    DRIVE = "Drive"
    ELECTRONICS = "Electronics"
    ENGINEER = "Engineer"
    EXPLOSIVES = "Explosives"
    FLYER = "Flyer"
    GAMBLER = "Gambler"
    GUNNER_TURRET = "Gunner(Turret)"
    GUNNER_ARTILLERY = "Gunner(Artillery)"
    GUN_ARCHAIC = "Gun Combat(Archaic)"
    GUN_ENERGY = "Gun Combat(Energy)"
    GUN_SLUG = "Gun Combat(Slug)"
    HEAVY_WEAPONS = "Heavy Weapons"
    INVESTIGATE = "Investigate"
    JACK_OF_ALL_TRADES = "Jack Of All Trades"
    LANGUAGE = "Language"
    LEADERSHIP = "Leadership"
    MECHANIC = "Mechanic"
    MEDIC = "Medic"
    MELEE = "Melee"
    NAVIGATION = "Navigation"
    PERSUADE = "Persuade"
    PILOT_SMALL = "Pilot(Small Craft)"
    PILOT_SPACE = "Pilot(Spacecraft)"
    PILOT_CAPITAL = "Pilot(Capital Ships)"
    PROFESSION = "Profession"
    RECON = "Recon"
    SCIENCE = "SCIENCE"
    SEAFARER = "Seafarer"
    STEALTH = "Stealth"
    STEWARD = "Steward"
    STREETWISE = "Streetwise"
    SURVIVAL = "Survival"
    TACTICS_MILITARY = "Tactics(Military)"
    TACTICS_NAVAL = "Tactics(Naval"
    VACC_SUIT = "Vacc Suit"


class Character:
    def __init__(self):
        self.stats = {"Strength": 0, "Endurance": 0, "Dexterity": 0, "Intelligence": 0, "Education": 0, "Society": 0,
                      "PSI": 0}
        self.name = ""
        self.species = ""
        self.age = 18
        self.skills = {}

