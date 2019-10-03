from py.system import *

int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]
int_to_bit_with_carry = lambda n : [n >> i & 1 for i in range(8,-1,-1)]

class ADC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute(self):
        a_vector = int_to_bit(self.system.getA())
        second_vector = int_to_bit(self.value_second)
        result = self.system.getA() + self.value_second + self.system.getFLAG("C")
        result_vector = int_to_bit(result)

        if ((a_vector[0] and second_vector[0] and not result_vector[0]) or (not a_vector[0] and not second_vector[0] and result_vector[0])):
            self.system.setFLAG("V", 1)
        else:
            self.system.setFLAG("V", 0)

        self.system.setFLAG("N", result_vector[0])
        if (all(value == 0 for value in result_vector)):
            self.system.setFLAG("Z", 1)
        else:
            self.system.setFLAG("Z", 0)


        self.system.setA(result)

        if (self.system.getA() % 256 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 256)
        else:
            self.system.setFLAG("C", 0)

class SBC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute(self):

        a_vector = int_to_bit(self.system.getA())
        second_vector = int_to_bit(self.value_second)
        result = self.system.getA() - self.value_second - (1 - self.system.getFLAG("C"))
        result_vector = int_to_bit(result)

        if ((a_vector[0] and second_vector[0] and not result_vector[0]) or (not a_vector[0] and not second_vector[0] and result_vector[0])):
            self.system.setFLAG("V", 1)
        else:
            self.system.setFLAG("V", 0)

        self.system.setFLAG("N", result_vector[0])
        if (all(value == 0 for value in result_vector)):
            self.system.setFLAG("Z", 1)
        else:
            self.system.setFLAG("Z", 0)


        self.system.setA(result)

        if (self.system.getA() % 256 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 256)
        else:
            self.system.setFLAG("C", 0)

class AddWithCarry0x61(ADC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(self, SystemCPU.loadMem(pos))


class AddWithCarry0x65(ADC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(zpg_pos))
        super().execute()


class AddWithCarry0x69(ADC_Op):
    def __init__(self, SystemCPU: System, imm: int):
        super().__init__(SystemCPU, imm)
        super().execute()


class AddWithCarry0x6D(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte))
        super().execute()

class AddWithCarry0x71(ADC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(self, SystemCPU.loadMem(pos))

class AddWithCarry0x75(ADC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(zpg_pos + SystemCPU.getX()))
        super().execute()

class AddWithCarry0x79(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte + SystemCPU.getY()))
        super().execute()

class AddWithCarry0x7D(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte + SystemCPU.getX()))
        super().execute()




class SubWithCarry0xE1(SBC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(pos))
        super().execute()


class SubWithCarry0xE5(SBC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(zpg_pos))
        super().execute()


class SubWithCarry0xE9(SBC_Op):
    def __init__(self, SystemCPU: System, imm: int):
            super().__init__(SystemCPU, imm)
            super().execute()


class SubWithCarry0xED(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte))
        super().execute()

class SubWithCarry0xF1(SBC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(pos))
        super().execute()

class SubWithCarry0xF5(SBC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(zpg_pos + SystemCPU.getX()))
        super().execute()

class SubWithCarry0xF9(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte + SystemCPU.getY()))
        super().execute()

class SubWithCarry0xFD(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(absHighByte * 256 + absLowByte + SystemCPU.getX()))
        super().execute()
