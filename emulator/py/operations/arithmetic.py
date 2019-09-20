class ADC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute():
        # A + M + C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)

class SBC_Op():
    value_second = 0
    system = ""
    def __init__(self, systemCPU: System, value_second: int):
        self.system = systemCPU
        self.value_second = value_second

    def execute():
        # A - M - C -> A, C
        # checar se teve overflow
        # atualizar valor de A
        print (self.operation)

class AddWithCarry0x61(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, SystemCPU.MEM[SystemCPU.getY()], "Op 61")


class AddWithCarry0x65(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, zpg_index, "Op 65")


class AddWithCarry0x69(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, imm, "Op 69")


class AddWithCarry0x6D(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs, "Op 6D")

class AddWithCarry0x71(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, Y[índex], "Op 71")

class AddWithCarry0x75(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, zpg_index[X], "Op 75")

class AddWithCarry0x79(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs[Y], "Op 79")

class AddWithCarry0x7D(ADC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs[X], "Op 7D")




class SubWithCarry0xE1(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, X[index], "Op E1")


class SubWithCarry0xE5(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, zpg_index, "Op E5")


class SubWithCarry0xE9(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, imm, "Op E9")


class SubWithCarry0xED(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs, "Op ED")

class SubWithCarry0xF1(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, Y[índex], "Op F1")

class SubWithCarry0xF5(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, zpg_index[X], "Op F5")

class SubWithCarry0xF9(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs[Y], "Op F9")

class SubWithCarry0xFD(SBC_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(self, abs[X], "Op FD")
