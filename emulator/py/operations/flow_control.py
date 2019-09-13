####################################
#  JUMP / BRANCH / RETURN / BREAK  #
####################################

class BRK0x00():
    def __init__(self, operation: str):
    print("BRK impl")

class BPL0x10():
    def __init__(self, operation: str):
    print("BPL rel")

class JSR0x20():
    def __init__(self, operation: str):
    print("JSR abs")

class BMI0x30():
    def __init__(self, operation: str):
    print("BMI rel")

class BVC0x50():
    def __init__(self, operation: str):
    print("BVC rel")

class RTS0x60():
    def __init__(self, operation: str):
    print("RTS impl")

class BVS0x70():
    def __init__(self, operation: str):
    print("BVS rel")

class BCC0x90():
    def __init__(self, operation: str):
    print("BCC rel")

class BCS0xB0():
    def __init__(self, operation: str):
    print("BCS rel")

class BNE0xD0():
    def __init__(self, operation: str):
    print("BNE rel")

class BEQ0xF0():
    def __init__(self, operation: str):
    print("BEQ rel")

class JMP_abs0x4C():
    def __init__(self, operation: str):
    print("JMP abs")

class JMP_ind0x6C():
    def __init__(self, operation: str):
    print("JMP ind")

class SEI0x78():
    def __init__(self, operation: str):
    print("SEI impl")
