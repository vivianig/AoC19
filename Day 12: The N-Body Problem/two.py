from math import gcd
class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0

    def move(self, ax):
        if ax == 0:
            self.x += self.v_x
        elif ax == 1:            
            self.y += self.v_y
        else:
            self.z += self.v_z


    def apply_gravity(self, moon, ax):
        if ax == 0:
            self.v_x += (1 if moon.x > self.x else -1 if moon.x < self. x else 0)
        elif ax == 1:            
            self.v_y += (1 if moon.y > self.y else -1 if moon.y < self. y else 0)
        else:
            self.v_z += (1 if moon.z > self.z else -1 if moon.z < self. z else 0)

    def encode(self, ax):
        if ax == 0:
            return("%d%d" % (self.x, self.v_x))
        elif ax == 1:
            return("%d%d" % (self.y, self.v_y))
        else:
            return("%d%d" % (self.z, self.v_z))
    
    def __str__(self):
        return("Position: %d,%d,%d\nVelocity:%d,%d,%d" % (self.x, self.y, self.z, self.v_x, self.v_y, self.v_z))
        
with open("input") as f:
    moons = [Moon(*[int(x[2:]) for x in line.strip()[1:-1].split(", ")]) for line in f.readlines()]

res = []
for ax in [0,1,2]:    
    counter = 0
    states = set()
    while(True):
        state = "".join([moon.encode(ax) for moon in moons])
        if state in states:
            break
        states.add(state)
        for a in moons:
            for b in moons:
                a.apply_gravity(b, ax)
        for moon in moons:
            moon.move(ax)
        counter+=1
    res.append(counter)



def lcm(a, b):
    return abs(a*b) // gcd(a, b)
print(lcm(res[0], lcm(res[1], res[2])))
