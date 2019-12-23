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
for centre in asteroids:
    angles = [degrees(atan2(asteroid[0] - centre[0], asteroid[1] - centre[1])) for asteroid in asteroids]
    if len(set(angles)) > max_view:
        max_view = len(set(angles))
        goal = centre

print(max_view, goal)
