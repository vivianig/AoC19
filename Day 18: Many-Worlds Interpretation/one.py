from math import inf
from functools import lru_cache
grid = {}
with open("input") as f:
    for y, line in enumerate(f.readlines()):
        for x, obj in enumerate(line.strip()):
            grid[x, y] = obj


directions = [(-1,0),(0,-1),(1,0),(0,1)]
neighbours = {}
keys = {}
for pos in grid:
    obj = grid[pos]
    if obj == "#":
        continue
    elif obj == "@":
        starting_pos = pos
    elif obj != "." and obj.islower():
        keys[obj] = pos
    neighbours[pos] = []
    for new_pos in [(pos[0]+x[0], pos[1]+x[1]) for x in directions]:
        if new_pos in grid and grid[new_pos] != "#":
            neighbours[pos].append(new_pos)
            
def print_map():
    min_x = min([x[0] for x in grid])
    max_x = max([x[0] for x in grid])
    min_y = min([x[1] for x in grid])
    max_y = max([x[1] for x in grid])
    for y in range(min_y, max_y+1):
        row = []
        for x in range(min_x, max_x+1):
            if grid[x,y] == ".":
                row.append(" ")
            else:
                row.append(grid[x,y])
        print("".join(row))    

def find_paths(starting_pos):
    paths = {}
    visited, queue = set([starting_pos]), [(n, [n], []) for n in neighbours[starting_pos]]
    while queue:
        pos, path, doors = queue.pop(0)
        if pos not in visited:
            obj = grid[pos]
            if obj != "." and obj != "@":
                if obj.islower():
                    if obj not in doors:
                        paths[obj] = (len(path), doors)
                else:
                    doors = doors + [obj.lower()]
            visited.add(pos)
            queue.extend([(new_pos, path + [new_pos], doors) for new_pos in neighbours[pos]])
    return paths

print_map()
map_paths = {"@": find_paths(starting_pos)}
for k in keys:
    map_paths[k] = find_paths(keys[k])

cache = {}

def explore_paths(current_obj, keys_found, steps_count):
    if (current_obj, keys_found) in cache :
        return cache[(current_obj, keys_found)]+steps_count
    if len(keys_found) == len(keys):
        return steps_count
    paths = map_paths[current_obj]
    available_paths = [path for path in paths if path not in keys_found and set(paths[path][1]).issubset(set(keys_found))]
    if not available_paths:
        return inf
    shortest_path = inf
    for new_obj in sorted(available_paths, key=lambda x:paths[x][0]):        
        shortest_path = min(shortest_path, explore_paths(new_obj, "".join(sorted(keys_found+new_obj)), paths[new_obj][0]))
    cache[(current_obj, keys_found)] = shortest_path
    return shortest_path+steps_count
        
shortest_path = explore_paths("@", "", 0)
print("Lenght shortest path", shortest_path)
