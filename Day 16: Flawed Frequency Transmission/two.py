with open("input") as f:
    inp = f.readline().strip() * 10000

offset = int(inp[:7])
inp = inp[offset:]

for z in range(100):
    out = []
    s = 0
    for i in range(len(inp)-1, -1, -1):
        s+= int(inp[i])
        out.append(+s)        
    out.reverse()
    inp = "".join([str(x)[-1] for x in out])

print(inp[:8])
