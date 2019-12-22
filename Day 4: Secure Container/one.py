inp = "136760-595730"

min_range = [int(x) for x in inp.split("-")[0]]
max_range = [int(x) for x in inp.split("-")[1]]
max_value = int(inp.split("-")[1])

current_range = min_range

def is_above_max_range(current_range):
    current_value = int("".join([str(x) for x in current_range]))
    return current_value > max_value
    
def increase_range(current_range):
    if current_range[-1] == 9:
        current_range = increase_range(current_range[:-1])
        current_range.append(current_range[-1])
    else:
        current_range[-1]+=1
    return current_range

def is_valid(current_range):
    for x in range(5):
        if current_range[x] > current_range[x+1]:
            return False
        elif current_range[x] == current_range[x+1]:
            return True
    return False

count = 0

while not is_above_max_range(current_range):
    if is_valid(current_range):
        count+=1
    current_range = increase_range(current_range)

print(count)
