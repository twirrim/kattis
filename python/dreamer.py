import sys
import calendar
from datetime import date
from itertools import permutations
from multiprocessing.dummy import Process, Queue

def is_valid_date(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def evaluate_perm(perm):
    day = int(''.join(perm[6:8]))
    month = int(''.join(perm[4:6]))
    year = int(''.join(perm[0:4]))
    if is_valid_date(day, month, year):
        output = "{:04d}{:02d}{:02d}".format(year, month, day)
        return output
    return None

def handle_test_case(test_case, case_number, queue):
    digits = test_case.replace(" ", "")
    possibles = set()
    for perm in set(permutations(digits)):
        if int(perm[0]) < 2 or int(perm[4]) > 1 or int(perm[6]) > 3:
            continue
        result = evaluate_perm(perm)
        if result:
            possibles.add(result)
    if possibles:
        poss = sorted(possibles)[0]
        output = (case_number,
                  "{} {} {} {}".format(len(possibles), poss[6:8], poss[4:6], poss[0:4]))
        queue.put(output)
    else:
        output = (case_number, "0")
        queue.put(output)

def main(test_cases):
    procs = []
    queue = Queue()
    case_number = 0
    for test_case in test_cases:
        proc = Process(target=handle_test_case, args=(test_case, case_number, queue))
        procs.append(proc)
        case_number += 1
    for proc in procs:
        proc.start()
    for proc in procs:
        proc.join()

    results = [queue.get() for proc in procs]
    results.sort()
    for r in results:
        print(r[1])


if __name__ == "__main__":
    throwaway = sys.stdin.readline()
    data = [line.rstrip() for line in sys.stdin.readlines()]
    main(data)
