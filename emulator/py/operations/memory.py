from py.system import *

class DEC_Op():
    system = ''
    position = 0
    def __init__(self, systemCPU: System, position: int):
        self.position = position
        self.system = systemCPU

    def execute(self):
        value = self.system.loadMem(self.position)
        value = value - 1
        if (value % 256!= value):
            self.system.setFLAG("C", 1)
        self.system.setMem(self.position, value % 256)
        if (self.system.loadMem(self.position) == 0):
            self.system.setFLAG("Z", 1)
        else:
            self.system.setFLAG("Z", 0)
        if (self.system.loadMem(self.position) > 127):
            self.system.setFLAG("N", 1)

class DEC_zero_page_0xC6(DEC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class DEC_absolute_0xCE(DEC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class DEC_zero_page_X_0xD6(DEC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class DEC_absolute_X_0xDE(DEC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class INC_Op():
    system = ''
    position = 0
    def __init__(self, systemCPU: System, position: int):
        self.position = position
        self.system = systemCPU

    def execute(self):
        value = self.system.loadMem(self.position)
        value = value + 1
        if (value % 256 != value):
            self.system.setFLAG("C", 1)
        self.system.setMem(self.position, value % 256)

        if (self.system.loadMem(self.position) == 0):
            self.system.setFLAG("Z", 1)
        else:
            self.system.setFLAG("Z", 0)

        if (self.system.loadMem(self.position) >= 128):
            self.system.setFLAG("N", 1)
        else:
            self.system.setFLAG("N", 0)

class INC_zero_page_0xE6(INC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class INC_absolute_0xEE(INC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class INC_zero_page_X_0xF6(INC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()

class INC_absolute_X_0xFE(INC_Op):
    def __init__(self, SystemCPU: System, pos: int):
        super().__init__(SystemCPU, pos)
        super().execute()
