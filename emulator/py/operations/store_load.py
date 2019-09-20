FromAclass Store_Op():
    register = ''
    position = 0
    operation = ''
    def __init__(self, register: str, position: int, operation: str):
        self.register = register
        self.position = position
        self.operation = operation

    def execute():
        # IF register = 'A', 'Y', 'X'
        # M = A
        print (self.operation)


# STA

class StoreInA0x81(Store_Op):
    def __init__(self, X: str, index: int, operation: str):
        super().__init__(self, 'A', X[index], "Op 81")


class StoreInA0x85(Store_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'A', zpg_index, "Op 85")


class StoreInA0x8D(Store_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'A', abs, "Op 8D")

class StoreInA0x91(Store_Op):
    def __init__(self, index: int, Y: int, operation: str):
        super().__init__(self, 'A', Y[index], "Op 91")

class StoreInA0x95(Store_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().__init__(self, 'A', zpg_index[X], "Op 95")

class StoreInA0x99(Store_Op):
    def __init__(self, imm: int, operation: str):
        super().__init__(self, 'A', imm, "Op 99")

class StoreInA0x9D(Store_Op):
    def __init__(self,  abs: int, X: int operation: str):
        super().__init__(self, 'A', abs[X], "Op 9D")

# STX

class StoreInX0x86(Store_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'X', zpg_index, "Op 86")

class StoreInX0x8E(Store_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'X', abs, "Op 8E")

class StoreInX0x96(Store_Op):
    def __init__(self, zpg_index: int, Y: int, operation: str):
        super().__init__(self, 'X', zpg_index[Y], "Op 96")

# STY

class StoreInY0x84(Store_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'Y', zpg_index, "Op 84")

class StoreInX0x8C(Store_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'Y', abs, "Op 8C")

class StoreInX0x94(Store_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().__init__(self, 'Y', zpg_index[X], "Op 94")




class Load_Op():
    register = ''
    position = 0
    operation = ''
    def __init__(self, register: str, position: int, operation: str):
        self.register = register
        self.position = position
        self.operation = operation

    def execute():
        # IF register = 'A', 'Y', 'X'
        # Y,Z,N = M
        print (self.operation)


class LoadFromA0xA1(Load_Op):
    def __init__(self, X: str, index: int, operation: str):
        super().__init__(self, 'A', X[index], "Op A1")

class LoadFromA0xA5(Load_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'A', zpg_index, "Op A5")

class LoadFromA0xA9(Load_Op):
    def __init__(self, imm: int, operation: str):
        super().__init__(self, 'A', imm, "Op A9")

class LoadInA0xAD(Load_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'A', abs, "Op AD")

class LoadFromA0xB1(Load_Op):
    def __init__(self, index: int, Y: int, operation: str):
        super().__init__(self, 'A', Y[index], "Op B1")

class LoadFromA0xB5(Load_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().__init__(self, 'A', zpg_index[X], "Op B5")

class LoadFromA0xB9(Load_Op):
    def __init__(self,  abs: int, Y: int operation: str):
        super().__init__(self, 'A', abs[Y], "Op B9")

class LoadInA0xBD(Load_Op):
    def __init__(self,  abs: int, X: int operation: str):
        super().__init__(self, 'A', abs[X], "Op BD")

class LoadFromX0xA2(Load_Op):
    def __init__(self, imm: int, operation: str):
        super().__init__(self, 'X', imm, "Op A2")

class LoadFromX0xA6(Load_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'X', zpg_index, "Op A6")

class LoadFromX0xB6(Load_Op):
    def __init__(self, zpg_index: int, Y: int, operation: str):
        super().__init__(self, 'X', zpg_index[Y], "Op B6")

class LoadFromX0xAE(Load_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'X', abs, "Op AE")

class LoadFromX0xBE(Load_Op):
    def __init__(self,  abs: int, Y: int operation: str):
        super().__init__(self, 'X', abs[Y], "Op BE")

class LoadFromY0xA0(Load_Op):
    def __init__(self, imm: int, operation: str):
        super().__init__(self, 'Y', imm, "Op A0")


class LoadFromY0xA4(Load_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().__init__(self, 'Y', zpg_index, "Op A4")

class LoadFromY0xAC(Load_Op):
    def __init__(self, abs: int, operation: str):
        super().__init__(self, 'Y', abs, "Op AC")

class LoadFromY0xB4(Load_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().__init__(self, 'Y', zpg_index[X], "Op B4")

class LoadFromY0xBC(Load_Op):
    def __init__(self,  abs: int, X: int operation: str):
        super().__init__(self, 'Y', abs[X], "Op BC")
