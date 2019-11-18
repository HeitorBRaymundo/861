import time
class System():
    A = 0
    X = 0
    Y = 0
    mem = [0] * 2048
    FLAGS = {"C": 0, "Z": 0, "I": 0, "D": 0, "B": 0, "O": 0, "N": 0}
    stack = []
    rom = None
    PC_OFFSET = 0
    SP_OFFSET = 0
    program_counter = 0
    stack_val_return = 0
    branch_hit = False
    stack_neg = False
    cycle_counter = 0
    _counter = 0
    time = -1
    def __init__ (self, rom):
        System._counter += 1
        self.id = System._counter
        self.A = 0
        self.X = 0
        self.Y = 0
        self.mem = [-1] * 2048
        self.FLAGS = {"N": 0, "V": 0, "B": 1, "D": 0, "I": 1, "Z": 0, "C": 0}
        self.stack = [0] * 512
        self.rom = rom
        self.PC_OFFSET = 0x8000 if (self.rom.prg_rom_size==2) else 0xC000
        self.program_counter = (self.rom.prg_rom[self.rom.interrupt_handlers['RESET_HANDLER'] + 1 - self.PC_OFFSET] << 8 + self.rom.prg_rom[self.rom.interrupt_handlers['RESET_HANDLER'] - self.PC_OFFSET]) - 0x8000
        self.stack_pointer = 0x01fd
        self.stack_val_return = 0
        self.branch_hit = False
        self.stack_neg = False
        self.ppu_set = 0
        self.time = -1
        self.cycle_counter = 0

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

    def stack_push(self, value, numBytes):
        if numBytes == 2:
            if value < 0:
                self.stack_neg = True

            hi, lo = (value & 0xffff).to_bytes(2, 'big')
            self.stack[self.stack_pointer] = hi
            self.stack[self.stack_pointer - 1] = lo
            self.stack_pointer = self.stack_pointer - 2
        else:
            self.stack[self.stack_pointer] = value
            self.stack_pointer = self.stack_pointer - 1

    def stack_pop(self):
        if len(self.stack) <= 0:
            raise Exception("Stack is empty!")
        else:
            self.stack_pointer = self.stack_pointer + 1
            return self.stack[self.stack_pointer]

    # Problema com a stack:
    # Valor que o SP anda depende do número de bytes lido ou salvo na pilha
    # Ideia de refactor: mudar a push para quebrar o valor que será guardado em bytes e salvar byte a byte na pilha
    # pop continua desempilhando 1 byte só e se precisarmos de mais, chamamos a pop mais de uma vez
    def getSP(self):
        return hex(self.stack_pointer) # com refactor não precisa desse 2 multiplicando (tamanho da pilha fica em bytes)

    def setMem(self, address, value):
        try:
            # map the addres between 0 to 0x0800
            if type(address) == str:
                converted_address = int(address, 16) & int('0x7ff', 16)
            else:
                converted_address = int(address) & int('0x7ff', 16)
        except:
            raise Exception('Invalid type of address!')

        if converted_address == 8:
            if self.loadMem(8) != value:
                if self.time == -1:
                    self.time = time.time()
                else:
                    last_time = self.time
                    self.time = time.time()
                    if self.time - last_time < 2:
                        # print('\t',self.time - last_time)
                        return
                        
                    
        try:
            # save the value
            self.mem[converted_address] = value
        except:
            raise Exception("Invalid address!")

    def loadMem(self, address):
        try:
            if not address == 0x2002:
                # map the addres between 0 to 0x0800
                if type(address) == str:
                    converted_address = int(address, 16) & int('0x7ff', 16)
                else:
                    converted_address = int(address) & int('0x7ff', 16)
            else:
                converted_address = address
        except:
            raise Exception('Invalid type of address!')

        # converted_address = address
        try:
            # save the value
            if converted_address == 0x2002:
                return self.rom.prg_rom[converted_address]
            else:
                return self.mem[converted_address]
        except:
            raise Exception("Invalid address!")
        #     return False


if __name__ == '__main__':
    system = System()
    # import pdb; pdb.set_trace()
