import sys, itertools
with open("input") as f:
    input_program = [int(x) for x in f.readline().split(",")]

class IntCodeComputer:

    def __init__(self):    
        self.params = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            99: 0
        }
        self.program = []
        self.pointer = 0

    def split_instruction(self, inst):
        inst = str(inst)
        op_code = int(inst[-2:])
        params_mode = [0] * self.params[op_code]
        params_inst = [int(x) for x in inst[:-2][::-1]]
        for i, mode in enumerate(params_inst):
            params_mode[i] = mode
        return (op_code, params_mode)

    #Return True if halting is invoked
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
            self.program[params[0]] = self.inputs.pop(0)
        elif op is 4:
            print("Output:", self.program[params[0]])
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
        elif op is 99:
            print("Halting")
            return True
        else:
            print("Unrecognized op", op)
            sys.exit(1)
        
    def execute(self, program, inputs):
        self.program = program
        self.inputs = inputs
        self.pointer = 0
        while(True):
            op, params_mode = self.split_instruction(self.program[self.pointer])
            params = []
            for mode in params_mode:
                self.pointer+=1
                if mode is 0:
                    params.append(self.program[self.pointer])
                elif mode is 1:
                    params.append(self.pointer)
            if self.execute_op(op, params):
               return self.output
            self.pointer +=1

computer = IntCodeComputer()
combinations = list(itertools.permutations(range(5), 5))
max_out = 0
for comb in combinations:
    out = 0
    for inp in comb:
        out = computer.execute(input_program, [inp, out])
    max_out = max(max_out, out)

print("Maximum input", max_out)
