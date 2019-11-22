int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

from py.system import *

class Increase_Op():
    register = ''
    system = ''
    def __init__(self, systemCPU: System, register: str):
        self.register = register
        self.system = systemCPU

    def execute(self):
        if (self.register == 'Y'):
            self.system.setY(self.system.getY() + 1)

            if self.system.getY() == 0:
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (self.system.getY() >= 128):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

        elif (self.register == 'X'):
            self.system.setX(self.system.getX() + 1)

            if self.system.getX() == 0:
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (self.system.getX() >= 128):
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)


class IncreaseReg0xC8(Increase_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'Y')
        super().execute()


class IncreaseReg0xE8(Increase_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'X')
        super().execute()

class Decrease_Op():
    register = ''
    system = ''
    def __init__(self, systemCPU: System, register: str):
        self.register = register
        self.system = systemCPU

    def execute(self):
        if (self.register == 'Y'):
            
            if (self.system.getY() - 1) < 0:
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)
            
            if (self.system.getY() - 1) == 0:
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            self.system.setY(self.system.getY() - 1)

        elif (self.register == 'X'):

            if (self.system.getX() - 1) == 0:
                self.system.setFLAG("Z", 1)
            else:
                self.system.setFLAG("Z", 0)

            if (self.system.getX() - 1) < 0:
                self.system.setFLAG("N", 1)
            else:
                self.system.setFLAG("N", 0)

            self.system.setX(self.system.getX() - 1)

class DecreaseReg0x88(Decrease_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'Y')
        super().execute()


class DecreaseReg0xCA(Decrease_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'X')
        super().execute()

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
