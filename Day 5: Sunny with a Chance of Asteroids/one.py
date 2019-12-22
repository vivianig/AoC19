import sys
with open("input") as f:
    input_program = [int(x) for x in f.readline().split(",")]

class IntCodeComputer:

    def __init__(self):    
        self.params = {
            1: 3,
            2: 3,
            3: 1,
            4: 1, 
            99: 0
        }
        self.program = []

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
            self.program[params[0]] = int(input("Input: "))
        elif op is 4:
            print("Output:", self.program[params[0]])
        elif op is 99:
            print("Halting")
            sys.exit(1)
        else:
            print("Unrecognized op", op)
            sys.exit(1)
        
    def execute(self):
        pointer = 0
        while(True):
            op, params_mode = self.split_instruction(self.program[pointer])
            params = []
            for mode in params_mode:
                pointer+=1
                if mode is 0:
                    params.append(self.program[pointer])
                elif mode is 1:
                    params.append(pointer)
            self.execute_op(op, params)
            pointer +=1

computer = IntCodeComputer()
computer.program = input_program
computer.execute()
