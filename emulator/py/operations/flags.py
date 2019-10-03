################################
#        FLAGS / STACK         #
################################
from py.system import *

int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

def int_to_string(n):
    return str(n)

def string_to_int(n):
    return int(n)

# OK
# tested
class PHP0x08():
    def __init__(self, system):
        # Push Processor Status on Stack
        # push SR
        systemRegister = [0, 0, 0, 0, 0, 0, 0, 0]
        systemRegister[7] = system.getFLAG("C")
        systemRegister[6] = system.getFLAG("Z")
        systemRegister[5] = system.getFLAG("I")
        systemRegister[4] = system.getFLAG("D")
        systemRegister[3] = system.getFLAG("B")
        systemRegister[2] = 1
        systemRegister[1] = system.getFLAG("V")
        systemRegister[0] = system.getFLAG("N")
        # systemRegister = [N,V,1,B,D,I,Z,C] here
        # print("systemRegister: ", systemRegister)

        systemRegisterStringArray = list(map(int_to_string, systemRegister))
        # systemRegisterStringArray = ['N','V','1','B','D','I','Z','C'] here
        # print("systemRegisterStringArray: ", systemRegisterStringArray)

        y = ""
        systemRegisterString = y.join(systemRegisterStringArray)
        # systemRegisterString = 'NV1BDIZC'
        # print("systemRegisterString: ", systemRegisterString)

        systemRegisterNumber = int(systemRegisterString, 2)
        # systemRegisterNumber = NV1BDIZC (as decimal int)
        # print("systemRegisterNumber: ", systemRegisterNumber)

        # print("vai pushar SR as number: ", systemRegisterNumber)
        # print("unpadded number ", systemRegisterNumber)

        system.stack_push(systemRegisterNumber)

# OK
# tested
class CLC0x18():
    def __init__(self, system):
        # Clear Carry Flag
        # 0 -> C
        system.setFLAG("C", 0)

# OK
# tested
class PLP0x28():
    def __init__(self, system):
        # Pull Processor Status from Stack
        # pull SR
        systemRegisterPopped = system.stack_pop()
        # print("systemRegisterPopped: ", systemRegisterPopped)

        systemRegisterNumber = int("{0:b}".format(systemRegisterPopped))
        # systemRegisterNumber = NV1BDIZC (as int)
        # OBS: if N or V = 0, systemRegisterNumber may have less than 8 bits
        # It cant have less than 6 bits because of the hardcoded 1
        # print("systemRegisterNumber: ", systemRegisterNumber)

        systemRegisterString = str('{0:08}'.format(systemRegisterNumber))
        # systemRegisterString = 'NV1BDIZC' already padded with zeros if N or V = 0
        # print("systemRegisterString: ", systemRegisterString)

        systemRegisterStringArray = list(systemRegisterString)
        # systemRegisterStringArray = ['N','V','1','B','D','I','Z','C'] here
        # print("systemRegisterStringArray: ", systemRegisterStringArray)

        systemRegisterNumberArray = list(map(string_to_int, systemRegisterStringArray))
        # print("systemRegisterNumberArray: ", systemRegisterNumberArray)

        system.setFLAG("C", systemRegisterNumberArray[7])
        system.setFLAG("Z", systemRegisterNumberArray[6])
        system.setFLAG("I", systemRegisterNumberArray[5])
        system.setFLAG("D", systemRegisterNumberArray[4])
        system.setFLAG("B", systemRegisterNumberArray[3])

        system.setFLAG("V", systemRegisterNumberArray[1])
        system.setFLAG("N", systemRegisterNumberArray[0])


# OK
# tested
class SEC0x38():
    def __init__(self, system):
        # Set Carry Flag
        # 1 -> C
        system.setFLAG("C", 1)

# OK
# tested
class PHA0x48():
    def __init__(self, system):
        # Push Accumulator on Stack
        # push A
        system.stack_push(system.getA())

# OK
# tested
class PLA0x68():
    def __init__(self, system):
        # Pull Accumulator from Stack
        # pull A
        acumulator = system.stack_pop()
        if (acumulator == 0):
            system.setFLAG("Z", 1)

        # print(acumulator)

        acumulatorBits = int_to_bit(acumulator)

        if (acumulatorBits[0] == 1):
            system.setFLAG("N", 1)

        system.setA(acumulator)

# OK
# tested
class CLV0xB8():
    def __init__(self, system):
        # Clear Overflow Flag
        # 0 -> V
        system.setFLAG("V", 0)

# OK
# tested
class CLD0xD8():
    def __init__(self, system):
        # Clear Decimal Mode
        # 0 -> D
        system.setFLAG("D", 0)

# OK
# tested
class SED0xF8():
    def __init__(self, system):
        # Set Decimal Flag
        # 1 -> D
        system.setFLAG("D", 1)
