with open("input") as f:
    modules = f.readlines()

print(sum([int(x)//3-2 for x in modules]))
