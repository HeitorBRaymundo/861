################################
#        FLAGS / STACK         #
################################

class PHP0x08():
    def __init__(self, operation: str):
        # Push Processor Status on Stack
        # push SR
        print("PHP impl")

class CLC0x18():
    def __init__(self, operation: str):
        # Clear Carry Flag
        # 0 -> C
        print("CLC impl")

class PLP0x28():
    def __init__(self, operation: str):
        # Pull Processor Status from Stack
        # pull SR
        print("PLP impl")

class SEC0x38():
    def __init__(self, operation: str):
        # Set Carry Flag
        # 1 -> C
        print("SEC impl")

class PHA0x48():
    def __init__(self, operation: str):
        # Push Accumulator on Stack
        # push A
        print("PHA impl")

class PLA0x68():
    def __init__(self, operation: str):
        # Pull Accumulator on Stack
        # pull A
        print("PLA impl")

class CLV0xB8():
    def __init__(self, operation: str):
        # Clear Overflow Flag
        # 0 -> V
        print("CLV impl")

class CLD0xD8():
    def __init__(self, operation: str):
        # Clear Decimal Mode
        # 0 -> D
        print("CLD impl")

class SED0xF8():
    def __init__(self, operation: str):
        # Set Decimal Flag
        # 1 -> D
        print("SED impl")
