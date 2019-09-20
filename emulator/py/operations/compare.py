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
        # A + M + C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)


class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, systemCPU: System, value_A: int, X: str, index: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 01", "ORA")
        super().execute

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op 05", "ORA")

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op 09", "ORA")

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op 0D", "ORA")

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, Y[index], "Op 11", "ORA")

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, systemCPU: System, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index[X], "Op 15", "ORA")

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 19", "ORA")

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs[Y], "Op 1D", "ORA")

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 21", "AND")

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, systemCPU: System, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op 25", "AND")

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op 29", "AND")

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op 2D", "AND")

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, Y[index], "Op 31", "AND")

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, systemCPU: System, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index[X], "Op 35", "AND")

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 39", "AND")

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs[Y], "Op 3D", "AND")

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 41", "EOR")

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op 45", "EOR")

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op 49", "EOR")

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op 4D", "EOR")

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, Y[index], "Op 51", "EOR")

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op 55", "EOR")

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, systemCPU: System, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index[X], "Op 59", "EOR")

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs[Y], "Op 5D", "EOR")

class CompareWithY0xC0(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op C0", "CPY")

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, systemCPU: System, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, X[index], "Op C1", "CMP")

class CompareWithY0xC4(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op C4", "CPY")

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op C5", "CMP")

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op C9", "CMP")

class CompareWithY0xCC(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op CC", "CPY")

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op CD", "CMP")

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, Y[index], "Op D1", "CMP")

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, systemCPU: System, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index[X], "Op D5", "CMP")

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, systemCPU: System, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs[Y], "Op D9", "CMP")

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, systemCPU: System, X: str, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs[X], "Op DD", "CMP")

class CompareWithX0xE0(CMP_Op):
    def __init__(self, systemCPU: System, imm: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, imm, "Op E0"), "CPX")
class CompareWithX0xE4(CMP_Op):
    def __init__(self, systemCPU: System, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, zpg_index, "Op E4", "CPX")

class CompareWithX0xEC(CMP_Op):
    def __init__(self, systemCPU: System, abs: int, value_A: int, operation: str):
        super().__init__(self, systemCPU, valueA, abs, "Op EC", "CPX")
