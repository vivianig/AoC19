from collections import OrderedDict

with open("input") as f:
    first_wire = f.readline().split(",")
    second_wire = f.readline().split(",")

def compute_path(wire):
    directions = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0)
    }
    current_x = current_y = 0
    # We can't convert to a set since sets are not otdered,
    # so insted we use a dictionary
    path = OrderedDict()
    steps = 0
    for op in wire:
        x, y = directions[op[0]]
        for i in range(int(op[1:])):
            steps +=1
            current_x += x
            current_y += y
            new_position = "%d,%d" % (current_x, current_y)
            if new_position not in path:
                path[new_position] = steps
    return path

first_path = compute_path(first_wire)
second_path = compute_path(second_wire)

crossings = [location for location in first_path.keys() if location in second_path]

print(min([first_path[location] + second_path[location] for location in crossings]))
