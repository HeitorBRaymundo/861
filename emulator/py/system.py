class System():
    A = 0
    X = 0
    Y = 0
    mem = [0] * 2048
    FLAGS = {"C": 0, "Z": 0, "I": 0, "D": 0, "B": 0, "O": 0, "N": 0}
    stack = []
    rom = None
    program_counter = 0

    def __init__ (self, rom):
        self.A = 0
        self.X = 0
        self.Y = 0
        self.mem = [0] * 2048
        self.FLAGS = {"N": 0, "V": 0, "B": 0, "D": 0, "I": 0, "Z": 0, "C": 0}
        self.stack = []
        self.rom = rom
        self.program_counter = (self.rom.prg_rom[self.rom.interrupt_handlers['RESET_HANDLER'] + 1 - 0x8000] << 8 + self.rom.prg_rom[self.rom.interrupt_handlers['RESET_HANDLER'] - 0x8000]) - 0xC000

    def getA(self):
        return self.A

    def setA(self, newA):
        self.A = newA

    def getX(self):
        return self.X

    def setX(self, newX):
        self.X = newX

    def getY(self):
        return self.Y

    def setY(self, newY):
        self.Y = newY

    def getFLAG(self, flag = 0):
        if (flag):
            return self.FLAGS[flag]

        return "{}{}{}{}{}{}{}".format(self.FLAGS["N"], self.FLAGS["V"], self.FLAGS["B"], self.FLAGS["D"], self.FLAGS["I"], self.FLAGS["Z"], self.FLAGS["C"],)

    def printFLAG(self, flag = 0):
        if (flag):
            return self.FLAGS[flag]

        return "{}{}1{}{}{}{}{}".format(self.FLAGS["N"], self.FLAGS["V"], self.FLAGS["B"], self.FLAGS["D"], self.FLAGS["I"], self.FLAGS["Z"], self.FLAGS["C"],)

    def setFLAG(self, flag, newValue):
        self.FLAGS[flag] = newValue

    def stack_push(self, value):
        if len(self.stack) > 256:
            raise Exception("Stack is already full!")
        else:
            self.stack.append(value)


    def stack_pop(self):
        if len(self.stack) <= 0:
            raise Exception("Stack is empty!")
        else:
            value = self.stack.pop()
            return value

    def getSP(self):
        return hex(0x1fd - len(self.stack) * 8)

    def setMem(self, address, value):
        try:
            # map the addres between 0 to 0x0800
            if type(address) == str:
                converted_address = int(address, 16) & int('0x7ff', 16)
            else:
                converted_address = int(address) & int('0x7ff', 16)
        except:
            raise Exception('Invalid type of address!')

        try:
            # save the value
            self.mem[converted_address] = value
        except:
            raise Exception("Invalid address!")

    def loadMem(self, address):
        try:
            # map the addres between 0 to 0x0800
            if type(address) == str:
                converted_address = int(address, 16) & int('0x7ff', 16)
            else:
                converted_address = int(address) & int('0x7ff', 16)
        except:
            raise Exception('Invalid type of address!')

        try:
            # save the value
            return self.mem[converted_address]
        except:
            raise Exception("Invalid address!")
            return False


if __name__ == '__main__':
    system = System()
    import pdb; pdb.set_trace()
