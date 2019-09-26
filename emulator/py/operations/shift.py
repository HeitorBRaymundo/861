from py.system import *

class ASL_Op():
    position = 0
    system = ''
    def __init__(self, systemCPU: System, position = -1):
        self.position = position
        self.system = systemCPU

    def execute(self):
        #  C <- [76543210] <- 0
        if (self.position == -1):
            if (self.system.getA() > 128):
                self.system.setFLAG("C", 1)
            self.system.setA((self.system.getA() << 1) % 255)
        else:
            if (self.system.loadMem(self.position) > 128):
                self.system.setFLAG("C", 1)
            self.system.setMem(self.position, (self.system.loadMem(self.position) << 1) % 255)

class ASL_zero_page_0x06(ASL_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos)
        super().execute()

class ASL_A_0x0A(ASL_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(SystemCPU)
        super().execute()

class ASL_absolute_0x0E(ASL_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class ASL_zero_page_index_0x16(ASL_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos + SystemCPU.getX())
        super().execute()

class ASL_abs_X_0x01E(ASL_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte + SystemCPU.getX())
        super().execute()

class ROL_Op():
    position = 0
    system = ''
    def __init__(self, systemCPU: System, position = -1):
        self.position = position
        self.system = systemCPU

    def execute(self):
        #  C <- [76543210] <- C
        isInCarry = self.system.getFLAG("C")
        if (self.position == -1):
            if (self.system.getA() > 128):
                self.system.setFLAG("C", 1)
            else:
                self.system.setFLAG("C", 0)
            self.system.setA(((self.system.getA() << 1)  + isInCarry) % 255)
        else:
            if (self.system.loadMem(self.position) > 128):
                self.system.setFLAG("C", 1)
            else:
                self.system.setFLAG("C", 0)
            self.system.setMem(self.position, ((self.system.loadMem(self.position) << 1)  + isInCarry) % 255)

class ROL_zero_page_0x26(ROL_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos)
        super().execute()

class ROL_A_0x2A(ROL_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(SystemCPU)
        super().execute()

class ROL_absolute_0x2E(ROL_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class ROL_zero_page_index_0x36(ROL_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos + SystemCPU.getX())
        super().execute()

class ROL_abs_X_0x3E(ROL_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte + SystemCPU.getX())
        super().execute()


class LSR_Op():
    position = 0
    system = ''
    def __init__(self, systemCPU: System, position = -1):
        self.position = position
        self.system = systemCPU

    def execute(self):
        #   0 -> [76543210] -> C
        if (self.position == -1):
            self.system.setFLAG("C", self.system.getA() % 2)
            self.system.setA(self.system.getA()  >> 1)
        else:
            self.system.setFLAG("C", self.system.loadMem(self.position) % 2)
            self.system.setMem(self.position, self.system.loadMem(self.position)  >> 1)

class LSR_zero_page_0x46(LSR_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos)
        super().execute()

class LSR_A_0x4A(LSR_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(SystemCPU)
        super().execute()

class LSR_absolute_0x4E(LSR_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class LSR_zero_page_index_0x56(LSR_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos + SystemCPU.getX())
        super().execute()

class LSR_abs_X_0x05E(LSR_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte + SystemCPU.getX())
        super().execute()


class ROR_Op():
    position = 0
    system = ''
    def __init__(self, systemCPU: System, position = -1):
        self.position = position
        self.system = systemCPU

    def execute(self):
        #   C -> [76543210] -> C
        if (self.position == -1):
            isInCarry = self.system.getFLAG("C") * 128
            self.system.setFLAG("C", self.system.getA() % 2)
            self.system.setA((self.system.getA()  >> 1) + isInCarry)
        else:
            isInCarry = self.system.getFLAG("C") * 128
            self.system.setFLAG("C", self.system.loadMem(system.position) % 2)
            self.system.setMem(self.position, self.system.loadMem(self.position)  >> 1 + isInCarry)

class ROR_zero_page_0x66(ROR_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, SystemCPU.loadMem(zpg_pos))
        super().execute()

class ROR_A_0x6A(ROR_Op):
    def __init__(self, SystemCPU: System):
        super().__init__(SystemCPU)
        super().execute()

class ROR_absolute_0x6E(ROR_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte)
        super().execute()

class ROR_zero_page_index_0x76(ROR_Op):
    def __init__(self, SystemCPU: System, zpg_pos: int):
        super().__init__(SystemCPU, zpg_pos + SystemCPU.getX())
        super().execute()

class ROR_abs_X_0x7E(ROR_Op):
    def __init__(self, SystemCPU: System, absLowByte: int, absHighByte: int):
        super().__init__(SystemCPU, absHighByte * 256 + absLowByte + SystemCPU.getX())
        super().execute()
