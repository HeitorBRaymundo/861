from py.system import *

class CMP_Op():
    first_value = 0
    second_value = 0
    group = ''
    def __init__(self, systemCPU: System, first_value: int, second_value: int, group: str):
        self.first_value = first_value
        self.second_value = second_value
        self.system = systemCPU
        self.group = group

    def execute(self):
        if (self.group == 'ORA'):
            res = self.first_value | self.second_value
            self.system.setA(res)
            if (not res):
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (res < 0):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

        elif (self.group == 'AND'):
            res = self.first_value & self.second_value
            self.system.setA(res)
            if (not res):
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (res < 0):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

        elif (self.group == 'EOR'):
            res = self.first_value ^ self.second_value
            self.system.setA(res)
            if (not res):
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (res < 0):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

        elif (self.group == 'CPY' or self.group == 'CMP' or self.group == 'CPX'):
            res = self.first_value - self.second_value
            if (self.first_value >= self.second_value):
                self.system.setFLAG("C", 1)
            else:
                self.system.setFLAG("C", 0)

            if (self.first_value == self.second_value):
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (res < 0):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getA(), imm, "ORA")
        super().execute()

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, systemCPU: System, addr: int):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr + systemCPU.getX()), "ORA")
        super().execute()

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "ORA")
        super().execute()

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getA(), imm, "AND")
        super().execute()

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr + systemCPU.getX()), "AND")
        super().execute()

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "AND")
        super().execute()

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), addr, "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getA(), imm, "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "EOR")
        super().execute()

class CompareWithY0xC0(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getY(), imm, "CPY")
        super().execute()

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithY0xC4(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getY(), systemCPU.loadMem(addr), "CPY")
        super().execute()

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getA(), imm, "CMP")
        super().execute()

class CompareWithY0xCC(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getY(), systemCPU.loadMem(addr), "CPY")
        super().execute()

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getA(), systemCPU.loadMem(addr), "CMP")
        super().execute()

class CompareWithX0xE0(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(systemCPU, systemCPU.getX(), imm, "CPX")
        super().execute()

class CompareWithX0xE4(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getX(), systemCPU.loadMem(addr), "CPX")
        super().execute()

class CompareWithX0xEC(CMP_Op):
    def __init__(self, systemCPU: System, addr):
        super().__init__(systemCPU, systemCPU.getX(), systemCPU.loadMem(addr), "CPX")
        super().execute()
