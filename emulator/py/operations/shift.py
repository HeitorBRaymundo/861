class ASL_Op():
    operation = ''
    position = 0
    def __init__(self, position: int, operation: str):
        self.position = position
        self.operation = operation

    def execute():
        #  C <- [76543210] <- 0
        print (self.operation)

class ASL_zero_page_0x06(ASL_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().init(self, zpg_index, "Op 06")

class ASL_A_0x0A(ASL_Op):
    def __init__(self, value_A: int, operation: str):
        super().init(self, value_A, "Op 0A")

class ASL_absolute_0x0E(ASL_Op):
    def __init__(self, abs: int, operation: str):
        super().init(self, abs, "Op 0E")

class ASL_zero_page_index_0x16(ASL_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().init(self, zpg_index[X], "Op 16")

class ASL_abs_X_0x01E(ASL_Op):
    def __init__(self, abs: int, X: int, operation: str):
        super().init(self, abs[X], "Op 1E")

class ROL_Op():
    operation = ''
    position = 0
    def __init__(self, position: int, operation: str):
        self.position = position
        self.operation = operation

    def execute():
        #  C <- [76543210] <- C
        print (self.operation)

class ROL_zero_page_0x26(ASL_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().init(self, zpg_index, "Op 26")

class ROL_A_0x2A(ASL_Op):
    def __init__(self, value_A: int, operation: str):
        super().init(self, value_A, "Op 2A")

class ROL_absolute_0x2E(ASL_Op):
    def __init__(self, abs: int, operation: str):
        super().init(self, abs, "Op 2E")

class ROL_zero_page_index_0x36(ASL_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().init(self, zpg_index[X], "Op 36")

class ROL_abs_X_0x03E(ASL_Op):
    def __init__(self, abs: int, X: int, operation: str):
        super().init(self, abs[X], "Op 3E")
