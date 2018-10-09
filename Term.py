from enum import Enum
import re

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

def article(string):
    if re.match(r"a|e|i|o|u|A|E|I|O|U", string[0]):
        return "an " + string
    else:
        return "a " + string

def advancement_string(com, adv, rank, rank_name, rank_bonus):
    string = ""
    if com is not "":
        if com is "Pass":
            string = "Became commissioned as {0} ({1})".format(article(rank_name), str(rank))
        else:
            string = "Failed to become commissioned"
    else:
        if adv is "Pass":
            string = "Advanced to {0} ({1})".format(rank_name, str(rank))
        else:
            string = "Failed to advance and remained {0} ({1})".format(article(rank_name), str(rank))

    if rank_bonus is not "":
        string += " and gained {0}.".format(rank_bonus)
    else:
        string += "."

    return string


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
        self.rank_name = ""
        self.rank_bonus = ""

    def __str__(self):
        if self.type is Type.NORMAL:
            return "In term {0}, served a normal term as {1} {2}. Trained in {3}. {4} the term. {5}. {6}".format(
                self.term_number, article(self.assignment.value), self.career.value, self.training, self.survival, self.event,
                advancement_string(self.commission, self.advancement, self.rank, self.rank_name, self.rank_bonus))
        elif self.type is Type.FIRST_TERM:
            return "In term {0}, served their first term as {1} {2}. Took basic training in {3}. {4} the term. {5}. {6}".format(
                self.term_number, article(self.assignment), self.career, self.training, self.survival,
                advancement_string(self.commission, self.advancement, self.rank, self.rank_name, self.rank_bonus))
        elif self.type is Type.PRE_CAREER:
            if self.career is Career.COLLEGE:
                "In term {0}, entered University and studied {1}. {2}. {3}".format(
                    self.term_number, self.training, self.event, self.advancement)
            elif self.career is Career.ACADEMY:
                "In term {0}, entered {1}".format(self.term_number, )

