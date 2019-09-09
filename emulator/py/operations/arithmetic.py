class Arithmetic():
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

class AddWithCarry0x61(Arithmetic):
    def __init__(self, carry: Boolean, X: str, index: int, value_A: int, operation: str):
        super().init(self, carry, valueA, X[index])
