from collections import namedtuple
from math import ceil

with open("input") as f:
    reaction_sheet = [x.strip() for x in f.readlines()]

Reaction = namedtuple("Reaction", ["out", "inputs"])

reactions = {}
for line in reaction_sheet:
    out = line.split("=> ")[1].split(" ")
    reactions[out[1]] = Reaction(int(out[0]), {x.split(" ")[1]: int(x.split(" ")[0])  for x in line.split(" =>")[0].split(", ")})


leftovers = {x: 0 for x in reactions}
def calculate_reaction(element, amount):
    if element == "ORE":
        return amount

    if leftovers[element] >= amount:
        leftovers[element]-=amount
        return 0
    elif leftovers[element] < amount:
        amount-=leftovers[element]
        leftovers[element] = 0

    r = reactions[element]
    n = ceil(amount/r.out)


    leftovers[element]+= (n*r.out)-amount
    return sum([calculate_reaction(x, r.inputs[x]*n) for x in r.inputs])

print(calculate_reaction("FUEL", 1))
    

