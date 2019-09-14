class ADC_Op():
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

class SBC_Op():
    is_carry_set = False
    value_A = 0
    value_second = 0
    operation = ''
    def __init__(self, is_carry_set: Boolean, value_A: int, value_second: int, operation: str):
        self.is_carry_set = is_carry_set
        self.value_A = value_A
        self.value_second = value_second

    def execute():
        # A - M - C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)

class AddWithCarry0x61(ADC_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, X[index], "Op 61")


class AddWithCarry0x65(ADC_Op):
    def __init__(self, carry: Boolean, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, zpg_index, "Op 65")


class AddWithCarry0x69(ADC_Op):
    def __init__(self, carry: Boolean, imm: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, imm, "Op 69")


class AddWithCarry0x6D(ADC_Op):
    def __init__(self, carry: Boolean, abs: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs, "Op 6D")

class AddWithCarry0x71(ADC_Op):
    def __init__(self, carry: Boolean, index: int, Y: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, Y[índex], "Op 71")

class AddWithCarry0x75(ADC_Op):
    def __init__(self, carry: Boolean, zpg_index: int, X: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, zpg_index[X], "Op 75")

class AddWithCarry0x79(ADC_Op):
    def __init__(self, carry: Boolean, abs: int, Y: int value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs[Y], "Op 79")

class AddWithCarry0x7D(ADC_Op):
    def __init__(self, carry: Boolean, abs: int, X: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs[X], "Op 7D")




class SubWithCarry0xE1(SBC_Op):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, X[index], "Op E1")


class SubWithCarry0xE5(SBC_Op):
    def __init__(self, carry: Boolean, zpg_index: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, zpg_index, "Op E5")


class SubWithCarry0xE9(SBC_Op):
    def __init__(self, carry: Boolean, imm: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, imm, "Op E9")


class SubWithCarry0xED(SBC_Op):
    def __init__(self, carry: Boolean, abs: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs, "Op ED")

class SubWithCarry0xF1(SBC_Op):
    def __init__(self, carry: Boolean, index: int, Y: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, Y[índex], "Op F1")

class SubWithCarry0xF5(SBC_Op):
    def __init__(self, carry: Boolean, zpg_index: int, X: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, zpg_index[X], "Op F5")

class SubWithCarry0xF9(SBC_Op):
    def __init__(self, carry: Boolean, abs: int, Y: int value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs[Y], "Op F9")

class SubWithCarry0xFD(SBC_Op):
    def __init__(self, carry: Boolean, abs: int, X: int, value_A: int, operation: str):
        super().__init__(self, carry, valueA, abs[X], "Op FD")
