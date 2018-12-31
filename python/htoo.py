import sys
import re
from collections import defaultdict

ATOM_RE = re.compile(r'((?P<molecule>\w)(?P<count>(\d+))?)')

def return_atom_dict(molecule, multiplier=1):
    primordial_goo = defaultdict(int)

    for atom in re.finditer(ATOM_RE, molecule):
        atom = atom.groupdict()
        if not atom['count']:
            atom['count'] = 1 * multiplier

        primordial_goo[atom['molecule']] += int(atom['count']) * multiplier

    return primordial_goo

input_molecule, number_of_input = sys.stdin.readline().rstrip().split(" ")
number_of_input = int(number_of_input)
desired_output = sys.stdin.readline().rstrip()

input_goo = return_atom_dict(input_molecule, number_of_input)
output_needs = return_atom_dict(desired_output)

minimum = sys.maxsize
for molecule in output_needs.keys():
    maximum_possible = int(input_goo[molecule]/output_needs[molecule])
    if minimum > maximum_possible:
        minimum = maximum_possible

print(minimum)
