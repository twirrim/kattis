import sys
from itertools import permutations
import logging

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return True

def is_valid_date(day, month, year):
    # Simple cases first
    if (day == 0 or day > 31):
        return False
    if (month == 0 or month > 12):
        return False
    if (year < 2000):
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return day <= 31
    elif month in [4, 6, 9, 11]:
        return day <= 30
    elif month == 2:
        if is_leap_year(year):
            return day <= 29
        return day <= 28
    return False

def evaluate_perm(perm):
    day = int(''.join(perm[6:8]))
    month = int(''.join(perm[4:6]))
    year = int(''.join(perm[0:4]))
    if is_valid_date(day, month, year):
        output = "{:04d}{:02d}{:02d}".format(year, month, day)
        return output
    return None


def main(test_cases):
    for test_case in test_cases:
        digits = test_case.replace(" ", "")
        possibles = set()
        seen = set()
        for perm in permutations(digits):
            if not perm in seen:
                seen.add(perm)
                result = evaluate_perm(perm)
                if result:
                    possibles.add(result)
            else:
                pass
        if possibles:
            poss = sorted(possibles)[0]
            print("{} {} {} {}".format(
                len(possibles), poss[6:8], poss[4:6], poss[0:4]))
        else:
            print(len(possibles))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    throwaway = sys.stdin.readline()
    data = [line.rstrip() for line in sys.stdin.readlines()]
    main(data)
