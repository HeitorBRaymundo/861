int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

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
    def __init__(self, first_register: str, second_register: str, system):
        self.first_register = first_register
        self.second_register = second_register
        self.system = system

    def execute(self):

        try:
            # get the value that will be transfer
            value = eval('self.system.' + self.first_register)
        except:
            raise Exception("Invalid register!")

        # set zero flag
        if value == 0:
            self.system.FLAGS["Z"] = 1
        else:
            self.system.FLAGS["Z"] = 0

        # set negative flag
        self.system.FLAGS["N"] = int_to_bit(value)[0]

        try:
            # transfer the value
            exec('self.system.' + self.second_register + '= value')
        except Exception as e:
            raise Exception("Invalid register!")

        return True


class Transfer_TXA_0x8A(Transfer_Op):
    def __init__(self, first_register: str, second_register: str, system):
        super().__init__(first_register, second_register, system)
        super().execute()

class Transfer_TYA_0x98(Transfer_Op):
    def __init__(self, first_register: str, second_register: str, system):
        super().__init__(first_register, second_register, system)
        super().execute()

class Transfer_TAY_0xA8(Transfer_Op):
    def __init__(self, first_register: str, second_register: str, system):
        super().__init__(first_register, second_register, system)
        super().execute()

class Transfer_TAX_0xAA(Transfer_Op):
    def __init__(self, first_register: str, second_register: str, system):
        super().__init__(first_register, second_register, system)
        super().execute()
