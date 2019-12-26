import sys
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


path = "L,12,L,8,R,10,R,10,L,6,L,4,L,12,L,12,L,8,R,10,R,10,L,6,L,4,L,12,R,10,L,8,L,4,R,10,L,6,L,4,L,12,L,12,L,8,R,10,R,10,R,10,L,8,L,4,R,10,L,6,L,4,L,12,R,10,L,8,L,4,R,10"


#Iteratively try any combination. Maximum lenght is 20. New patterns are considered
#only from the start (minus previous patterns) as the entire path has to be replaced
def compress_string(path):
    a_split = path.split(",")
    for i in range(10,1,-2):
        a_pattern = ",".join(a_split[0:i])
        if len(a_pattern) > 20:
            continue
        a_path = path.replace(a_pattern, "|")
        while a_path.startswith("|"):
            a_path = a_path[2:]

        b_split = a_path.split(",")
        for j in range(min(10, len(a_path)),1,-2):
            b_pattern = ",".join(b_split[0:j])
            if len(b_pattern) > 20  or "|" in b_pattern:
                continue
            b_path = a_path.replace(b_pattern, "|")
            while b_path.startswith("|"):
                b_path = b_path[2:]

            c_split = b_path.split(",")
            for k in range(min(10, len(b_path)),1,-2):
                c_pattern = ",".join(c_split[0:k])
                if len(c_pattern) > 20 or "|" in c_pattern:
                    continue
                c_path = b_path.replace(c_pattern, "|")
                if c_path.replace("|", "").replace(",", "") == "":
                    routine = path.replace(a_pattern, "A").replace(b_pattern, "B").replace(c_pattern, "C")
                    return (routine, a_pattern, b_pattern, c_pattern)

def convert_compression(compression):
    inputs = []
    for c in compression:
        inputs.extend([ord(x) for x in c]+ [10])
    #could't figure out live feed :(
    inputs.extend([44, ord("n"), 44, 10])
    return inputs

input_program[0] = 2
compression  = compress_string(path)
computer = IntCodeComputer(input_program.copy())

last_out = None
computer.execute(convert_compression(compression))
while True:
    out = computer.execute()
    if computer.halted:
        break
    last_out = out
print(last_out)
