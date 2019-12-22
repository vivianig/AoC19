with open("input") as f:
    computer = [int(x) for x in f.readline().split(",")]

computer[1] = 12
computer[2] = 2

pointer = 0
while True:
    value = computer[pointer]
    if value is 99:
        break
    elif value is 1:
        val_1 = computer[computer[pointer+1]]
        val_2 = computer[computer[pointer+2]]
        computer[computer[pointer+3]] = val_1 + val_2
    elif value is 2:
        val_1 = computer[computer[pointer+1]]
        val_2 = computer[computer[pointer+2]]
        computer[computer[pointer+3]] = val_1 * val_2
        
    pointer+=4

print(computer)
