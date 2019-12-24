class Moon:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0

    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z


    def apply_gravity(self, moon):
        self.v_x += (1 if moon.x > self.x else -1 if moon.x < self. x else 0)
        self.v_y += (1 if moon.y > self.y else -1 if moon.y < self. y else 0)
        self.v_z += (1 if moon.z > self.z else -1 if moon.z < self. z else 0)

    def total_energy(self):
        potential_energy = abs(self.x) + abs(self.y) + abs(self.z)
        kinetic_energy = abs(self.v_x) + abs(self.v_y) + abs(self.v_z)
        return potential_energy * kinetic_energy
    
    def __str__(self):
        return("Position: %d,%d,%d\nVelocity:%d,%d,%d" %(self.x, self.y, self.z, self.v_x, self.v_y, self.v_z))
        
with open("input") as f:
    moons = [Moon(*[int(x[2:]) for x in line.strip()[1:-1].split(", ")]) for line in f.readlines()]
    
for i in range(1000):
    for a in moons:
        for b in moons:
            a.apply_gravity(b)
    for moon in moons:
        moon.move()

print(sum([moon.total_energy() for moon in moons]))
