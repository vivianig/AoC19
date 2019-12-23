from math import atan2, degrees
with open("input") as f:
    asteroid_map = [[point for point in line.strip()] for line in f.readlines()]

asteroids = []
for j, row in enumerate(asteroid_map):
    for i, point in enumerate(row):
        if point == "#":
            asteroids.append((i,j))

max_view = 0
goal = None
to_be_destroyed = []
for centre in asteroids:
    angles = {}
    for asteroid in asteroids:
        if asteroid == centre:
            continue
        angle = degrees(atan2(asteroid[0] - centre[0], asteroid[1] - centre[1]))
        if angle not in angles:
            angles[angle] = []
        distance = abs(asteroid[0] - centre[0]) + abs(asteroid[1] -centre[1])
        angles[angle].append((asteroid, distance))
    if len(set(angles)) > max_view:
        max_view = len(set(angles))        
        to_be_destroyed = {x: sorted(angles[x], key=lambda z: z[1]) for x in angles}
        goal = centre

angles = sorted(to_be_destroyed.keys(), key=lambda x: x+180+360 if x <= 180 else x+180, reverse=True)
destroy_goal = 200
while max_view < destroy_goal:
    destroy_goal-=max_view
    for x in angles:
        print(x, to_be_destroyed[x].pop(0))
        if not to_be_destroyed[x]:
            del to_be_destroyed[x]

for x in range(destroy_goal):
    destroyed = to_be_destroyed[angles[x]].pop(0)
print(destroyed[0][0] * 100 + destroyed[0][1])
