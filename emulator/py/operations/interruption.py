################################
#         INTERUPTIONS         #
################################

from py.system import *

class RTI0x40():
    def __init__(self, system):
        # Return from Interrupt
        # pull SR
        systemRegister = system.stack_pop()

        system.setFLAG("C", systemRegister[0])
        system.setFLAG("Z", systemRegister[1])
        system.setFLAG("I", systemRegister[2])
        system.setFLAG("D", systemRegister[3])
        system.setFLAG("B", systemRegister[4])
        system.setFLAG("V", systemRegister[5])
        system.setFLAG("N", systemRegister[6])

        # restore PC from stack
        pc = system.stack_pop()
        # TODO restore PC


        # print("RTI impl")

# OK
class CLI0x58():
    def __init__(self, system):
        # Clear Interrupt Disable Bit
        # 0 -> I
        system.setFLAG("I", 0)
        print("CLI impl")
