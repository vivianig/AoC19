import sys, itertools,random
with open("input") as f:
    input_program = [int(x) for x in f.readline().split(",")]

class IntCodeComputer:

    def __init__(self, program, phase):
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
        self.program = program
        self.pointer = 0
        self.halted = False
        self.output = None
        self.inputs = [phase]

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
            self.halted = True
        else:
            print("Unrecognized op", op)
            sys.exit(1)
        
    def execute(self, inputs):
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
            self.execute_op(op, params)
            self.pointer +=1
        return self.output

combinations = list(itertools.permutations(range(5,10), 5))
max_out = 0
for phases in combinations:
    out = 0
    computers = [IntCodeComputer(input_program.copy(), phases[i]) for i in range(5)]
    last_out = 0
    while any([not computer.halted for computer in computers]):
        for computer in computers:
            out = computer.execute([out])
        if out:
            last_out = out
    max_out = max(max_out, last_out)

    
print("Maximum input", max_out)
