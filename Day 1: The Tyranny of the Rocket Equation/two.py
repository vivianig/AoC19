def fuel_formula(x):
    total_fuel = x//3-2
    missing_fuel = total_fuel
    while missing_fuel > 0:
        missing_fuel = missing_fuel//3-2
        if missing_fuel <=0:
            continue
        total_fuel += missing_fuel
    return total_fuel

with open("input") as f:
    modules = f.readlines()


print(sum([fuel_formula(int(x)) for x in modules]))




