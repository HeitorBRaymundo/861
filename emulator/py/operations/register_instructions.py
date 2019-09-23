from py.system import *

class Increase_Op():
    register = ''
    system = ''
    def __init__(self, systemCPU: System, register: str):
        self.register = register
        self.system = systemCPU

    def execute(self):
        if (self.register == 'Y'):
            print (self.system.getY())
            self.system.setY(self.system.getY() + 1)
            if (self.system.getY() % 255 != self.system.getY()):
                self.system.setY(self.system.getY() % 255)
                self.system.setFLAG("C", 1)
            print (self.system.getY())
        elif (self.register == 'X'):
            print (self.system.getX())
            self.system.setX(self.system.getX() + 1)
            if (self.system.getX() % 255 != self.system.getX()):
                self.system.setX(self.system.getX() % 255)
                self.system.setFLAG("C", 1)
            print (self.system.getX())

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
            print (self.system.getY())
            self.system.setY(self.system.getY() - 1)
            if (self.system.getY() < 0):
                self.system.setFLAG("N", 1)
            if (self.system.getY() % 255 != self.system.getY()):
                self.system.setY(self.system.getY() % 255)
                self.system.setFLAG("C", 1)
            print (self.system.getY())
        elif (self.register == 'X'):
            print (self.system.getX())
            self.system.setX(self.system.getX() - 1)
            if (self.system.getX() < 0):
                self.system.setFLAG("N", 1)
            if (self.system.getX() % 255 != self.system.getX()):
                self.system.setX(self.system.getX() % 255)
                self.system.setFLAG("C", 1)
            print (self.system.getX())

class DecreaseReg0x88(Decrease_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'Y')
        super().execute()


class DecreaseReg0xCA(Decrease_Op):
    def __init__(self, systemCPU: System):
        super().__init__(systemCPU, 'X')
        super().execute()

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
