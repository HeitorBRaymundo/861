################################
#         INTERUPTIONS         #
################################

from py.system import *

class RTI0x40():
    def __init__(self, system):
        # Return from Interrupt
        # pull SR, pull PC
        print("RTI impl")

class CLI0x58():
    def __init__(self, system):
        # Clear Interrupt Disable Bit
        # 0 -> I
        super().setFLAG("I", 0)
        print("CLI impl")
