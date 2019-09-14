################################
#         INTERUPTIONS         #
################################

class RTI0x40(System):
    def __init__(self, operation: str):
        # Return from Interrupt
        # pull SR, pull PC
        print("RTI impl")

class CLI0x58(System):
    def __init__(self, operation: str):
        # Clear Interrupt Disable Bit
        # 0 -> I
        super().setFLAG("I", 0)
        print("CLI impl")
