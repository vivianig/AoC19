with open("input") as f:
    orbit_map = [x.strip().split(")") for x in f.readlines()]
    
orbits = {y: [] for x, y in orbit_map}


for x, y in orbit_map:
    orbits[y] = x

def build_path(current_object, path):
    while current_object != "COM":
        path.append(current_object)
        current_object = orbits[current_object]
    return path
    
path_from_you = build_path("YOU", [])
path_from_san = build_path("SAN", [])

intersection = [x for x in path_from_you if x in path_from_san][0]
print(path_from_you.index(intersection) + path_from_san.index(intersection) - 2)
