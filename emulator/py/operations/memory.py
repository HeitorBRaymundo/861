class DEC_Op():
    operation = ''
    position = 0
    def __init__(self, position: int, operation: str):
        self.position = position
        self.operation = operation

    def execute():
        # M - 1 -> M
        print (self.operation)

class DEC_zero_page_0xC6(DEC_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().init(self, zpg_index, "Op C6")

class DEC_A_0xCE(DEC_Op):
    def __init__(self, abs: int, operation: str):
        super().init(self, abs, "Op CE")

class DEC_absolute_0xD6(DEC_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().init(self, zpg_index[X], "Op D6")

class DEC_zero_page_index_0xDE(DEC_Op):
    def __init__(self, abs: int, X: int, operation: str):
        super().init(self, abs[X], "Op DE")

class INC_Op():
    operation = ''
    position = 0
    def __init__(self, position: int, operation: str):
        self.position = position
        self.operation = operation

    def execute():
        # M + 1 -> M
        print (self.operation)

class INC_zero_page_0xE6(INC_Op):
    def __init__(self, zpg_index: int, operation: str):
        super().init(self, zpg_index, "Op E6")

class INC_A_0xEE(INC_Op):
    def __init__(self, abs: int, operation: str):
        super().init(self, abs, "Op EE")

class INC_absolute_0xF6(INC_Op):
    def __init__(self, zpg_index: int, X: int, operation: str):
        super().init(self, zpg_index[X], "Op F6")

class INC_zero_page_index_0xEE(INC_Op):
    def __init__(self, abs: int, X: int, operation: str):
        super().init(self, abs[X], "Op FE")
