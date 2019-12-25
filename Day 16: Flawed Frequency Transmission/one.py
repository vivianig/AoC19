with open("input") as f:
    inp = f.readline().strip()

base_pattern = (0, 1, 0, -1)

for z in range(100):
    out = []
    for i in range(len(inp)):
        # Generate pattern by multiplying each element of it by the number of the input digit being processed
        pattern = [x for y in base_pattern for x in [y]*(i+1)]
        # Instead of eliminating the first pattern digit only on the first iteration, we duplicate the pattern
        # until the lenght is sufficient and ignore the first digit only once
        while len(pattern) < len(inp)+1:
            pattern = pattern*2
        # Execute the entire calculation of the output in a single sweep. The string is split into digits,
        # the digits are converted to integer ands multiplied by the pattern, the results are summed and
        # converted back to string to easily keep only the smallest digit
        out.append(str(sum([int(x)*pattern[j+1] for j, x in enumerate(inp)]))[-1])

    inp = "".join(out)

print(inp[:8])
