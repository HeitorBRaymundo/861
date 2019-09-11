class Increase_Op():
    register = ''
    operation = ''
    def __init__(self, register: str, operation: str):
        self.register = register

    def execute():
        # value_register ++
        print (self.operation)

class IncreaseReg0xC8(Increase_Op):
    def __init__(self):
        super().init(self, 'Y', "Op C8")


class IncreaseReg0xE8(Increase_Op):
    def __init__(self):
        super().init(self, 'X', "Op E8")

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
        super().init(self, 'Y', "Op 88")


class IncreaseReg0xCA(Decrease_Op):
    def __init__(self):
        super().init(self, 'X', "Op CA")

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


class IncreaseReg0x8A(Transfer_Op):
    def __init__(self):
        super().init(self, 'X', 'A', "Op 8A")

class IncreaseReg0x98(Transfer_Op):
    def __init__(self):
        super().init(self, 'Y', 'A', "Op CA")

class IncreaseReg0xA8(Transfer_Op):
    def __init__(self):
        super().init(self, 'A', 'Y', "Op CA")

class IncreaseReg0xAA(Transfer_Op):
    def __init__(self):
        super().init(self, 'A', 'X', "Op CA")
