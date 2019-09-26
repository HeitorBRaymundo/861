################################
#        FLAGS / STACK         #
################################

from py.system import *

class PHP0x08():
    def __init__(self, system):
        # Push Processor Status on Stack
        # push SR
        print("PHP impl")

class CLC0x18():
    def __init__(self, system):
        # Clear Carry Flag
        # 0 -> C
        super().setFLAG("C", 0)
        print("CLC impl")

class PLP0x28():
    def __init__(self, system):
        # Pull Processor Status from Stack
        # pull SR
        print("PLP impl")

class SEC0x38():
    def __init__(self, system):
        # Set Carry Flag
        # 1 -> C
        super().setFLAG("C", 1)
        print("SEC impl")

class PHA0x48():
    def __init__(self, system):
        # Push Accumulator on Stack
        # push A
        print("PHA impl")

class PLA0x68():
    def __init__(self, system):
        # Pull Accumulator on Stack
        # pull A
        print("PLA impl")

class CLV0xB8():
    def __init__(self, system):
        # Clear Overflow Flag
        # 0 -> V
        super().setFLAG("V", 0)
        print("CLV impl")

class CLD0xD8():
    def __init__(self, system):
        # Clear Decimal Mode
        # 0 -> D
        super().setFLAG("D", 0)
        print("CLD impl")

class SED0xF8():
    def __init__(self, system):
        # Set Decimal Flag
        # 1 -> D
        super().setFLAG("D", 1)
        print("SED impl")
