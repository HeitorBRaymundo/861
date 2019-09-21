from py import system

class CMP_Op():
    first_value = 0
    second_value = 0
    group = ''
    def __init__(self, systemCPU: System, first_value: int, second_value: int, group: str):
        self.first_value = first_value
        self.second_value = second_value
        self.system = systemCPU
        self.group = group

    def execute():
        if (self.group == 'ORA'):

        elif (self.group == 'AND'):

        elif (self.group == 'CPY'):

        elif (self.group == 'CMP'):

        elif (self.group == 'CPX'):

class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "ORA")
        super().execute()

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "ORA")
        super().execute()

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "ORA")
        super().execute()

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "ORA")
        super().execute()

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "ORA")
        super().execute()

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "ORA")
        super().execute()

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getY() + index], "ORA")
        super().execute()

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "ORA")
        super().execute()

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "AND")
        super().execute()

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "AND")
        super().execute()

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "AND")
        super().execute()

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "AND")
        super().execute()

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getY() + index], "AND")
        super().execute()

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "AND")
        super().execute()

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getY()], "AND")
        super().execute()

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "AND")
        super().execute()

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), zpg_index, "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), abs, "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getY()], "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getX()], "EOR")
        super().execute()

class CompareWithY0xC0(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "CPY")
        super().execute()

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index + systemCPU.getX()], "CMP")
        super().execute()

class CompareWithY0xC4(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "CPY")
        super().execute()

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "CMP")
        super().execute()

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "CMP")
        super().execute()

class CompareWithY0xCC(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "CPY")
        super().execute()

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "CMP")
        super().execute()

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "CMP")
        super().execute()

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "CMP")
        super().execute()

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "CMP")
        super().execute()

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "CMP")
        super().execute()

class CompareWithX0xE0(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), "CPX")
        super().execute()

class CompareWithX0xE4(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "CPX")
        super().execute()

class CompareWithX0xEC(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "CPX")
        super().execute()
