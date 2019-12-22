with open("input") as f:
    base_computer = [int(x) for x in f.readline().split(",")]

goal = 19690720

for noun in range(100):
    for verb in range(100):
        computer = [x for x in base_computer]
        computer[1] = noun
        computer[2] = verb

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

        if computer[0] == goal:
            print(100 * noun + verb)
