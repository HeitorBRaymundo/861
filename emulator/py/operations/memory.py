from py.system import *

class DEC_Op():
    system = ''
    position = 0
    def __init__(self, systemCPU: System, position: int):
        self.position = position
        self.system = systemCPU

    def execute(self):
        # M - 1 -> M
        print (self.operation)

class DEC_zero_page_0xC6(DEC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(systemCPU, zpg_index)
        super().execute()

class DEC_absolute_0xCE(DEC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class DEC_zero_page_X_0xD6(DEC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU, zpg_index + X)
        super().execute()

class DEC_absolute_X_0xDE(DEC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU,  absHighByte * 256 + absLowByte)
        super().execute()

class INC_Op():
    system = ''
    position = 0
    def __init__(self, systemCPU: System, position: int):
        self.position = position
        self.system = systemCPU

    def execute(self):
        # M + 1 -> M
        print (self.operation)

class INC_zero_page_0xE6(INC_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(systemCPU, zpg_index)
        super().execute()

class INC_absolute_0xEE(INC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class INC_zero_page_X_0xF6(INC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU, zpg_index + X)
        super().execute()

class INC_absolute_X_0xFE(INC_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(systemCPU,  absHighByte * 256 + absLowByte)
        super().execute()
