################################
#         INTERUPTIONS         #
################################

class RTI0x40():
    def __init__(self, operation: str):
        # Return from Interrupt
        # pull SR, pull PC
        print("RTI impl")

class CLI0x58():
    def __init__(self, operation: str):
        # Clear Interrupt Disable Bit
        # 0 -> I
        print("CLI impl")
