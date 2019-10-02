from py.system import *

int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

class ADC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute(self):
        if (self.system.getA() < 127 and self.value_second < 127 and (self.system.getA() + self.value_second) >= 128):
            self.system.setFLAG("V", 1)

        self.system.setA(self.system.getA() + self.system.getFLAG("C") + self.value_second)

        if (self.system.getA() % 256 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 256)

        if self.system.getA() == 0:
            self.system.setFLAG("Z", 1)
        else:
            self.system.setFLAG("Z", 0)

        if (self.system.getA() > 127):
            self.system.setFLAG("N", 1)

class SBC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute(self):
        self.system.setA(self.system.getA() - (1 - self.system.getFLAG("C")) - self.value_second)
        if (self.system.getA() < 0):
            self.system.setFLAG("N", 1)

        if self.system.getA() == 0:
            self.system.setFLAG("Z", 1)

        if (self.system.getA() % 256 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 256)

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
