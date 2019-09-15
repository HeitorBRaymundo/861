from py.system import *

class Increase_Op(System):
    register = ''
    operation = ''
    def __init__(self, register: str, operation: str):
        self.register = register
        self.operation = operation
        self.execute(register)

    def execute(self, register):
        if (self.register == 'Y'):
            print (super().getY())
            super().setY(super().getY() + 1)
            print (super().getY())
        elif (self.register == 'X'):
            print (super().getX())
            super().setX(super().getX() + 1)
            print (super().getX())
        # value_register ++

        print (self.operation)

class IncreaseReg0xC8(Increase_Op):
    def __init__(self):
        super().__init__('Y', "Op C8")


class IncreaseReg0xE8(Increase_Op):
    def __init__(self):
        super().__init__(self, 'X', "Op E8")

class Decrease_Op():
    register = ''
    operation = ''
    def __init__(self, register: str, operation: str):
        self.register = register

    def execute():
        # value_register --
        print (self.operation)

class IncreaseReg0x88(Decrease_Op):
    def __init__(self):
        super().__init__(self, 'Y', "Op 88")


class IncreaseReg0xCA(Decrease_Op):
    def __init__(self):
        super().__init__(self, 'X', "Op CA")

class Transfer_Op():
    first_register = ''
    second_register = ''
    operation = ''
    def __init__(self, first_register: str, second_register: str, operation: str):
        self.first_register = first_register
        self.second_register = second_register

    def execute():
        # first, second = second, first
        print (self.operation)


class Transfer_TXA_0x8A(Transfer_Op):
    def __init__(self):
        super().__init__(self, 'X', 'A', "Op 8A")

class Transfer_TYA_0x98(Transfer_Op):
    def __init__(self):
        super().__init__(self, 'Y', 'A', "Op 98")

class Transfer_TAY_0xA8(Transfer_Op):
    def __init__(self):
        super().__init__(self, 'A', 'Y', "Op A8")

class Transfer_TAX_0xAA(Transfer_Op):
    def __init__(self):
        super().__init__(self, 'A', 'X', "Op AA")
