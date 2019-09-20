class CMP_Op():
    value_A = 0
    value_second = 0
    operation = ''
    def __init__(self, value_A: int, value_second: int, operation: str):
        self.value_A = value_A
        self.value_second = value_second

    def execute():
        # A + M + C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)


class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, value_A: int, X: str, index: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 01")

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op 05")

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op 09")

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op 0D")

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, Y[index], "Op 11")

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index[X], "Op 15")

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 19")

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs[Y], "Op 1D")

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 21")

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op 25")

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op 29")

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op 2D")

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, Y[index], "Op 31")

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index[X], "Op 35")

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 39")

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs[Y], "Op 3D")

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 41")

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op 45")

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op 49")

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op 4D")

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, Y[index], "Op 51")

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op 55")

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index[X], "Op 59")

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs[Y], "Op 5D")

class CompareWithY0xC0(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op C0")

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, X[index], "Op C1")

class CompareWithY0xC4(CMP_Op):
    def __init__(self, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op C4")

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op C5")

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op C9")

class CompareWithY0xCC(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op CC")

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op CD")

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, Y: str, index: int, value_A: int, operation: str):
        super().__init__(self, valueA, Y[index], "Op D1")

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, X: str, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index[X], "Op D5")

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, Y: str, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs[Y], "Op D9")

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, X: str, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs[X], "Op DD")

class CompareWithX0xE0(CMP_Op):
    def __init__(self, imm: int, value_A: int, operation: str):
        super().__init__(self, valueA, imm, "Op E0")`
class CompareWithX0xE4(CMP_Op):
    def __init__(self, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, valueA, zpg_index, "Op E4")

class CompareWithX0xEC(CMP_Op):
    def __init__(self, abs: int, value_A: int, operation: str):
        super().__init__(self, valueA, abs, "Op EC")
