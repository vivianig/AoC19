import sys
with open("input") as f:
    input_program = [int(x) for x in f.readline().split(",")]

class IntCodeComputer:

    def __init__(self, program, get_input=None):
        self.params = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            9: 1,
            99: 0
        }
        self.program = program
        self.program.extend([0]*10000)
        self.pointer = 0
        self.halted = False
        self.inputs = []
        self.get_input = get_input
        self.relative_base = 0
        self.output = None

    def split_instruction(self, inst):
        inst = str(inst)
        op_code = int(inst[-2:])
        params_mode = [0] * self.params[op_code]
        params_inst = [int(x) for x in inst[:-2][::-1]]
        for i, mode in enumerate(params_inst):
            params_mode[i] = mode
        return (op_code, params_mode)

    def execute_op(self, op, params):
        if op is 1:
            val_1 = self.program[params[0]]
            val_2 = self.program[params[1]]
            self.program[params[2]] = val_1 + val_2
        elif op is 2:
            val_1 = self.program[params[0]]
            val_2 = self.program[params[1]]
            self.program[params[2]] = val_1 * val_2
        elif op is 3:
            self.program[params[0]] = self.inputs.pop(0) if self.inputs else self.get_input()
        elif op is 4:
            self.output = self.program[params[0]]
        elif op is 5:            
            if self.program[params[0]] != 0:                
                self.pointer = self.program[params[1]] -1
        elif op is 6:
            if self.program[params[0]] == 0: 
                self.pointer = self.program[params[1]] -1
        elif op is 7:
            val_1 = self.program[params[0]]
            val_2 = self.program[params[1]]
            if val_1 < val_2:
                self.program[params[2]] = 1
            else:
                self.program[params[2]] = 0
        elif op is 8:
            val_1 = self.program[params[0]]
            val_2 = self.program[params[1]]
            if val_1 == val_2:
                self.program[params[2]] = 1
            else:
                self.program[params[2]] = 0
        elif op is 9:
            self.relative_base += self.program[params[0]]
        elif op is 99:
            print("Halting")
            self.halted = True
        else:
            print("Unrecognized op", op)
            sys.exit(1)
        
    def execute(self, inputs=[]):
        self.inputs.extend(inputs)
        self.output = None
        while not self.halted and self.output == None:
            op, params_mode = self.split_instruction(self.program[self.pointer])
            params = []
            for mode in params_mode:
                self.pointer+=1
                if mode is 0:
                    params.append(self.program[self.pointer])
                elif mode is 1:
                    params.append(self.pointer)
                elif mode is 2:
                    params.append(self.program[self.pointer]+self.relative_base)
            self.execute_op(op, params)
            self.pointer +=1
        return self.output


def is_intersection(pos):
    if grid[pos] != "#":
        return False
    for new_pos in [(pos[0] + offset[0], pos[1] + offset[1]) for offset in directions]:
        if grid[new_pos] != "#":
            return False
    return True

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    
computer = IntCodeComputer(input_program.copy())
camera = []
grid = {}
x = y = 0
while True:
    out = computer.execute()
    if computer.halted:
        break
    if out == 10:
        x = 0
        y += 1
    else:
        grid[(x,y)] = chr(out)
        x+=1
    camera.append(chr(out))
print("".join(camera))

alignment = 0
max_x = max([x[0] for x in grid])
max_y = max([x[1] for x in grid])
for j in range(1, max_y):
    for i in range(1, max_x):
        if is_intersection((i,j)):
            alignment+=i*j
print(alignment)
            
            
