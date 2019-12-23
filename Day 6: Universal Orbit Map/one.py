with open("input") as f:
    orbit_map = [x.strip().split(")") for x in f.readlines()]

is_orbited_by = {y: [] for x, y in orbit_map}
is_orbited_by["COM"] = []

for x, y in orbit_map:
    is_orbited_by[x].append(y)

orbit_count = {x: 0 for x, y in orbit_map}


stack = ["COM"]

while stack:
    current_object = stack.pop(0)
    stack.extend(is_orbited_by[current_object])
    for orbiter in is_orbited_by[current_object]:
        orbit_count[orbiter] = orbit_count[current_object] + 1


print(sum([orbit_count[x] for x in orbit_count]))
            
