from py.system import *

class ADC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute(self):
        self.system.setA(self.system.getA() + self.system.getFLAG("C") + self.value_second)
        if (self.system.getA() % 255 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 255)

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

        if (self.system.getA() % 255 != self.system.getA()):
            self.system.setFLAG("C", 1)
            self.system.setA(self.system.getA() % 255)

class AddWithCarry0x61(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, SystemCPU.MEM[SystemCPU.getY()], "Op 61")


class AddWithCarry0x65(ADC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(zpg_pos))
        super().execute()


class AddWithCarry0x69(ADC_Op):
    def __init__(self, SystemCPU: System, imm: int):
        super().__init__(SystemCPU, imm)
        super().execute()


class AddWithCarry0x6D(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte))
        super().execute()

class AddWithCarry0x71(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, Y[indrect], "Op 71")

class AddWithCarry0x75(ADC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(zpg_pos + SystemCPU.getX()))
        super().execute()

class AddWithCarry0x79(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte + SystemCPU.getY()))
        super().execute()

class AddWithCarry0x7D(ADC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte + SystemCPU.getX()))
        super().execute()




class SubWithCarry0xE1(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, X[index], "Op E1")


class SubWithCarry0xE5(SBC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(zpg_pos))
        super().execute()


class SubWithCarry0xE9(SBC_Op):
    def __init__(self, SystemCPU: System, imm: int):
            super().__init__(SystemCPU, imm)
            super().execute()


class SubWithCarry0xED(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte))
        super().execute()

class SubWithCarry0xF1(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, Y[índex], "Op F1")

class SubWithCarry0xF5(SBC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(zpg_pos + SystemCPU.getX()))
        super().execute()

class SubWithCarry0xF9(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte + SystemCPU.getY()))
        super().execute()

class SubWithCarry0xFD(SBC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, SystemCPU.getMEM(absHighByte * 256 + absLowByte + SystemCPU.getX()))
        super().execute()
