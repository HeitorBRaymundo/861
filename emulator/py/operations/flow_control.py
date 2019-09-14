####################################
#  JUMP / BRANCH / RETURN / BREAK  #
####################################

class BRK0x00(System):
    def __init__(self, operation: str):
        # Force Break
        # interrupt,                       N Z C I D V
        # push PC+2, push SR               - - - 1 - -
        print("BRK impl")

class BPL0x10(System):
    def __init__(self, operation: str):
        # Branch on Result Plus
        # branch on N = 0
        print("BPL rel")

class JSR0x20(System):
    def __init__(self, operation: str):
        # Jump to New Location Saving Return Address
        # push (PC+2),                     N Z C I D V
        # (PC+1) -> PCL                    - - - - - -
        # (PC+2) -> PCH
        print("JSR abs")

class BMI0x30(System):
    def __init__(self, operation: str):
        # Branch on Result Minus
        # branch on N = 1
        print("BMI rel")

class BVC0x50(System):
    def __init__(self, operation: str):
        # Branch on Overflow Clear
        # branch on V = 0
        print("BVC rel")

class RTS0x60(System):
    def __init__(self, operation: str):
        # Return from Subroutine
        # pull PC, PC+1 -> PC
        print("RTS impl")

class BVS0x70(System):
    def __init__(self, operation: str):
        # Branch on Overflow Set
        # branch on V = 1
        print("BVS rel")

class BCC0x90(System):
    def __init__(self, operation: str):
        # Branch on Carry Clear
        # branch on C = 0
        print("BCC rel")

class BCS0xB0(System):
    def __init__(self, operation: str):
        # Branch on Carry Set
        # branch on C = 1
        print("BCS rel")

class BNE0xD0(System):
    def __init__(self, operation: str):
        # Branch on Result not Zero
        # branch on Z = 0
        print("BNE rel")

class BEQ0xF0(System):
    def __init__(self, operation: str):
        # Branch on Result Zero
        # branch on Z = 1
        print("BEQ rel")

class JMP_abs0x4C(System):
    def __init__(self, operation: str):
        # Jump to New Location
        # (PC+1) -> PCL
        # (PC+2) -> PCH
        print("JMP abs")

class JMP_ind0x6C(System):
    def __init__(self, operation: str):
        print("JMP ind")

class SEI0x78(System):
    def __init__(self, operation: str):
        # Set Interrupt Disable Status
        # 1 -> I
        print("SEI impl")
