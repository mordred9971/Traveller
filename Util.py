import random


def mod(stat):
    if stat == 0:
        return -3
    elif stat in range(1, 2):
        return -2
    elif stat in range(3, 5):
        return -1
    elif stat in range(6, 8):
        return 0
    elif stat in range(9, 11):
        return 1
    elif stat in range(12 - 14):
        return +2
    else:
        return +3


def Roll(num, repeat, mod):
    result = []
    for i in range(repeat):
        hold = 0
        for n in range(num):
            hold += random.randint(1, 6)
        hold += mod
        result.append(hold)
    return result
