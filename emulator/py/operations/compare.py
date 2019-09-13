## fala galera

class CMP_Op():
    is_carry_set = False
    value_A = 0
    value_second = 0
    operation = ''
    def __init__(self, is_carry_set: Boolean, value_A: int, value_second: int, operation: str):
        self.is_carry_set = is_carry_set
        self.value_A = value_A
        self.value_second = value_second

    def execute():
        # A + M + C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)


class OrWithAcumulator0x01(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 01")

class OrWithAcumulator0x05(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 05")

class OrWithAcumulator0x09(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 09")

class OrWithAcumulator0x0D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 0D")

class OrWithAcumulator0x11(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 11")

class OrWithAcumulator0x15(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 15")

class OrWithAcumulator0x19(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 19")

class OrWithAcumulator0x1D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 1D")

class AndWithAcumulator0x21(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 21")

class AndWithAcumulator0x25(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 25")

class AndWithAcumulator0x29(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 29")

class AndWithAcumulator0x2D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 2D")

class AndWithAcumulator0x31(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 31")

class AndWithAcumulator0x35(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 35")

class AndWithAcumulator0x39(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 39")

class AndWithAcumulator0x3D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 3D")

class ExclusiveOrWithAcumulator0x41(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 41")

class ExclusiveOrWithAcumulator0x45(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 45")

class ExclusiveOrWithAcumulator0x49(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 49")

class ExclusiveOrWithAcumulator0x4D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 4D")

class ExclusiveOrWithAcumulator0x51(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 51")

class ExclusiveOrWithAcumulator0x55(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 55")

class ExclusiveOrWithAcumulator0x59(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 59")

class ExclusiveOrWithAcumulator0x5D(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op 5D")

class CompareWithY0xC0(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op C0")

class CompareWithY0xC4(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op C4")

class CompareWithY0xCC(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op CC")

class CompareWithAcumulator0xC1(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op C1")

class CompareWithAcumulator0xC5(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op C5")

class CompareWithAcumulator0xC9(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op C9")

class CompareWithAcumulator0xCD(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op CD")

class CompareWithAcumulator0xD1(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op D1")

class CompareWithAcumulator0xD5(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op D5")

class CompareWithAcumulator0xD9(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op D9")

class CompareWithAcumulator0xDD(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op DD")

class CompareWithX0xE0(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op E0")

class CompareWithX0xE4(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op E4")

class CompareWithX0xEC(CMP_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index], "Op EC")
