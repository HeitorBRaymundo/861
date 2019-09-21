from py import system

class CMP_Op():
    value_A = 0
    value_second = 0
    operation = ''
    group = ''
    def __init__(self, systemCPU: System, value_A: int, value_second: int, operation: str, group: str):
        self.value_A = value_A
        self.value_second = value_second
        self.system = systemCPU
        self.group = group

    def execute():
        if (self.group == 'ORA'):

        elif (self.group == 'AND'):

        elif (self.group == 'CPY'):

        elif (self.group == 'CMP'):

        elif (self.group == 'CPX'):

        # A + M + C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)


class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "Op 01", "ORA")
        super().execute()

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "Op 05", "ORA")
        super().execute()

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "Op 09", "ORA")
        super().execute()

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op 0D", "ORA")
        super().execute()

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "Op 11", "ORA")
        super().execute()

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "Op 15", "ORA")
        super().execute()

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getY() + index], "Op 19", "ORA")
        super().execute()

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op 1D", "ORA")
        super().execute()

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "Op 21", "AND")
        super().execute()

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "Op 25", "AND")
        super().execute()

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, systemCPU: System, imm: int):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "Op 29", "AND")
        super().execute()

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op 2D", "AND")
        super().execute()

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getY() + index], "Op 31", "AND")
        super().execute()

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "Op 35", "AND")
        super().execute()

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getY()], "Op 39", "AND")
        super().execute()

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op 3D", "AND")
        super().execute()

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[systemCPU.getX() + index], "Op 41", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), zpg_index, "Op 45", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "Op 49", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), abs, "Op 4D", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "Op 51", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "Op 55", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getY()], "Op 59", "EOR")
        super().execute()

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs + systemCPU.getX()], "Op 5D", "EOR")
        super().execute()

class CompareWithY0xC0(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "Op C0", "CPY")
        super().execute()

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index + systemCPU.getX()], "Op C1", "CMP")
        super().execute()

class CompareWithY0xC4(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "Op C4", "CPY")
        super().execute()

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "Op C5", "CMP")
        super().execute()

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), imm, "Op C9", "CMP")
        super().execute()

class CompareWithY0xCC(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op CC", "CPY")
        super().execute()

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op CD", "CMP")
        super().execute()

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, systemCPU: System, index: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[index] + systemCPU.getY(), "Op D1", "CMP")
        super().execute()

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index + systemCPU.getX()], "Op D5", "CMP")
        super().execute()

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op D9", "CMP")
        super().execute()

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, systemCPU: System, abs: int):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op DD", "CMP")
        super().execute()

class CompareWithX0xE0(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), "Op E0", "CPX")
        super().execute()

class CompareWithX0xE4(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[zpg_index], "Op E4", "CPX")
        super().execute()

class CompareWithX0xEC(CMP_Op):
    def __init__(self, systemCPU: System):
        super().__init__(self, systemCPU, systemCPU.getA(), systemCPU.getMEM()[abs], "Op EC", "CPX")
        super().execute()
