class Intcode:
    def __init__(self, instructons):
        self.memory = instructons
        self.instructionPointer = 0
        self.outputs = []
        self.inputs = []

    def run(self):
        inputPointer = 0
        opCode, modes = self.processOpCode(self.memory[0])

        while(opCode != 99):
            if (opCode == 1): #add
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                value = param1 + param2
                self.setValue(3, modes, value)
                self.instructionPointer += 4
            elif (opCode == 2): #multiply
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                value = param1 * param2
                self.setValue(3, modes, value)
                self.instructionPointer += 4
            elif (opCode == 3): #input
                self.setValue(1, modes, self.inputs[inputPointer])
                inputPointer += 1
                self.instructionPointer += 2
            elif (opCode == 4): #output
                result = self.getParameterValue(1, modes)
                self.instructionPointer += 2
                self.outputs.append(result)
            elif (opCode == 5): #jump if true
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                if param1 != 0:
                    self.instructionPointer = param2
                else:
                    self.instructionPointer +=3
            elif (opCode == 6): #jump if false
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                if param1 == 0:
                    self.instructionPointer = param2
                else:
                    self.instructionPointer += 3
            elif (opCode == 7): #less than
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                val = 1 if param1 < param2 else 0
                self.setValue(3, modes, val)
                self.instructionPointer += 4
            elif (opCode == 8): #equal to
                param1 = self.getParameterValue(1, modes)
                param2 = self.getParameterValue(2, modes)
                val =  1 if param1 == param2 else 0
                self.setValue(3, modes, val)
                self.instructionPointer += 4
            else:
                break

            opCode, modes = self.processOpCode(self.memory[self.instructionPointer])

    def addInput(self, value):
        self.inputs.append(value)

    def getParameterValue(self, paramNumber, modes):
        if modes[paramNumber - 1] == 0:
            return self.memory[self.memory[self.instructionPointer + paramNumber]]
        if modes[paramNumber - 1] == 1:
            return self.memory[self.instructionPointer + paramNumber]

    def setValue(self, paramNumber, modes, value):
        if modes[paramNumber - 1] == 1:
            self.memory[self.instructionPointer + paramNumber] = value
        elif modes[paramNumber - 1] == 0:
            self.memory[self.memory[self.instructionPointer + paramNumber]] = value

    def processOpCode(self, value):
        #pad zeros
        value = f'{value:05}'
        digits = [int(digit) for digit in value]
        #last 2 are always opCode
        opCode = int(str(digits[-2] + digits[-1]))
        modes = (digits[2], digits[1], digits[0])
        return opCode, modes