class Intcode:
    def __init__(self, instructons):
        self.memory = instructons
        self.instructionPointer = 0

    def run(self, input = 0):
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
            else:
                break

            opCode, modes = self.processOpCode(self.memory[self.instructionPointer])

    def getParameterValue(self, paramNumber, modes):
        if modes[paramNumber - 1] == 0:
            return self.memory[self.memory[self.instructionPointer + paramNumber]]
        if modes[paramNumber - 1] == 1:
            return self.memory[self.instructionPointer + paramNumber]

    def setValue(self, paramNumber, modes, value):
        if modes[paramNumber - 1] == 1:
            self.memory[self.instructionPointer + 3] = value
        elif modes[paramNumber - 1] == 0:
            self.memory[self.memory[self.instructionPointer + 3]] = value

    def processOpCode(self, value):
        #pad zeros
        value = f'{value:05}'
        digits = [int(digit) for digit in value]
        #last 2 are always opCode
        opCode = int(str(digits[-2] + digits[-1]))
        modes = (digits[2], digits[1], digits[0])
        return opCode, modes