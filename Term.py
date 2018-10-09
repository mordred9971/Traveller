from enum import Enum

class Type(Enum):
    NORMAL = "normal term"
    PRE_CAREER = "pre-career education"
    FIRST_TERM = "first term"
    STARTED_CAREER = "started career"
    DRAFT = "draft"
    PRISON = "served time in prison"
    DRIFT = "drifter"

class Career(Enum):
    COLLEGE = "University"
    ACADEMY = "Military Academy"
    AGENT = "Agent"
    ARMY = "Army"
    CITIZEN = "Citizen"
    DRIFTER = "Drifter"
    ENTERTAINER = "Entertainer"

class Assignment(Enum):
    ACADEMY_ARMY = "Army Academy"
    ACADEMY_MARINES = "Marines Academy"
    ACADEMY_NAVY = "Naval Academy"
    LAW_ENFORCEMENT = "Law Enforcement"

def careerString(career, assignment)
class Term:


    def __init__(self):
        self.qualified = ""
        self.type = ""
        self.career = ""
        self.assignment = ""
        self.term_number = 0
        self.training = ""
        self.survival = ""
        self.event = ""
        self.advancement = ""
        self.commission = ""
        self.rank = ""
        self.rank_bonus = ""

    def __str__(self):
        if type is Type.NORMAL:
            "In term {0}, served a normal term as a {1}".format(self.term_number, careerString(self.career, self.assignment))