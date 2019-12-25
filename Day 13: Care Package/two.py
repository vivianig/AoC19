import sys, itertools,random
import time
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

graphics = {
    0: " ",
    1: "|",
    2: "#",
    3: "_",
    4: "O"
}

    
def print_game():
    rows = []
    for y in range(22):
        row = []
        for x in range(38):
            row.append(graphics[grid[(x,y)] if (x,y) in grid else 0])
        rows.append("".join(row))
    print("\n".join(rows))

input_program[0] = 2
computer = IntCodeComputer(input_program.copy(), lambda: (ball_x > paddle_x) - (ball_x < paddle_x))

grid = {}
counter = 0
while not computer.halted:
    x = computer.execute()
    if x == None:
        break
    y = computer.execute()
    if x == -1 and y == 0:
        score = computer.execute()
    else:                       
        tile = computer.execute()
        if tile == 4:
            ball_x = x
        elif tile == 3:
            paddle_x = x
        grid[(x,y)] = tile        
    print_game()
print(score)

