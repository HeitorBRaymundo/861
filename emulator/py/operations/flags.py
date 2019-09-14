################################
#        FLAGS / STACK         #
################################

class PHP0x08(System):
    def __init__(self, operation: str):
        # Push Processor Status on Stack
        # push SR
        print("PHP impl")

class CLC0x18(System):
    def __init__(self, operation: str):
        # Clear Carry Flag
        # 0 -> C
        super().setFLAG("C", 0)
        print("CLC impl")

class PLP0x28(System):
    def __init__(self, operation: str):
        # Pull Processor Status from Stack
        # pull SR
        print("PLP impl")

class SEC0x38(System):
    def __init__(self, operation: str):
        # Set Carry Flag
        # 1 -> C
        super().setFLAG("C", 1)
        print("SEC impl")

class PHA0x48(System):
    def __init__(self, operation: str):
        # Push Accumulator on Stack
        # push A
        print("PHA impl")

class PLA0x68(System):
    def __init__(self, operation: str):
        # Pull Accumulator on Stack
        # pull A
        print("PLA impl")

class CLV0xB8(System):
    def __init__(self, operation: str):
        # Clear Overflow Flag
        # 0 -> V
        super().setFLAG("V", 0)
        print("CLV impl")

class CLD0xD8(System):
    def __init__(self, operation: str):
        # Clear Decimal Mode
        # 0 -> D
        super().setFLAG("D", 0)
        print("CLD impl")

class SED0xF8(System):
    def __init__(self, operation: str):
        # Set Decimal Flag
        # 1 -> D
        super().setFLAG("D", 1)
        print("SED impl")
