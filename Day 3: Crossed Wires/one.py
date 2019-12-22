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
    path = []

    for op in wire:
        x, y = directions[op[0]]
        for i in range(int(op[1:])):
            current_x += x
            current_y += y
            # Positions are stored as strings as they are hashable.
            # This allows quicker lookup and coverting the array to a set,
            # that is faster than checking every element at add time.
            new_position = "%d,%d" % (current_x, current_y)
            path.append(new_position)

    return set(path)

first_path = compute_path(first_wire)
second_path = compute_path(second_wire)

crossings = [location.split(",") for location in first_path if location in second_path]

print(min([abs(int(location[0])) + abs(int(location[1])) for location in crossings]))


