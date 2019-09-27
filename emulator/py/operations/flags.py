################################
#        FLAGS / STACK         #
################################

from py.system import *

int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

# OK
class PHP0x08():
    def __init__(self, system):
        # Push Processor Status on Stack
        # push SR
        systemRegister = [0, 0, 0, 0, 0, 0, 0]
        systemRegister[0] = system.getFLAG("C")
        systemRegister[1] = system.getFLAG("Z")
        systemRegister[2] = system.getFLAG("I")
        systemRegister[3] = system.getFLAG("D")
        systemRegister[4] = system.getFLAG("B")
        systemRegister[5] = system.getFLAG("V")
        systemRegister[6] = system.getFLAG("N")

        system.stack_push(systemRegister)

# OK
class CLC0x18():
    def __init__(self, system):
        # Clear Carry Flag
        # 0 -> C
        system.setFLAG("C", 0)

# OK
class PLP0x28():
    def __init__(self, system):
        # Pull Processor Status from Stack
        # pull SR
        systemRegister = system.stack_pop()

        system.setFLAG("C", systemRegister[0])
        system.setFLAG("Z", systemRegister[1])
        system.setFLAG("I", systemRegister[2])
        system.setFLAG("D", systemRegister[3])
        system.setFLAG("B", systemRegister[4])
        system.setFLAG("V", systemRegister[5])
        system.setFLAG("N", systemRegister[6])


# OK
class SEC0x38():
    def __init__(self, system):
        # Set Carry Flag
        # 1 -> C
        system.setFLAG("C", 1)

# OK
class PHA0x48():
    def __init__(self, system):
        # Push Accumulator on Stack
        # push A
        system.stack_push(system.getA())

# OK
class PLA0x68():
    def __init__(self, system):
        # Pull Accumulator from Stack
        # pull A
        acumulator = system.stack_pop()
        if (acumulator == 0):
            system.setFLAG("Z", 1)

        if (int_to_bit(value_to_load)[0] == 1):
            system.setFLAG("N", 1)

        system.setA(acumulator)

# OK
class CLV0xB8():
    def __init__(self, system):
        # Clear Overflow Flag
        # 0 -> V
        system.setFLAG("V", 0)

# OK
class CLD0xD8():
    def __init__(self, system):
        # Clear Decimal Mode
        # 0 -> D
        system.setFLAG("D", 0)

# OK
class SED0xF8():
    def __init__(self, system):
        # Set Decimal Flag
        # 1 -> D
        system.setFLAG("D", 1)
