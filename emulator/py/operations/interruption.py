################################
#         INTERUPTIONS         #
################################

from py.system import *

# OK
class RTI0x40():
    def __init__(self, system):
        # Return from Interrupt
        # pull SR
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

        # restore PC from stack
        lo = systemCPU.stack_pop()
        hi = systemCPU.stack_pop()
        hi = hi << 8

        if systemCPU.stack_neg:
            systemCPU.program_counter = - (((hi | lo) ^ 0xfff) + 1)
        else:
            systemCPU.program_counter = hi | lo

# OK
# tested
class CLI0x58():
    def __init__(self, system):
        # Clear Interrupt Disable Bit
        # 0 -> I
        system.setFLAG("I", 0)
        # print("CLI impl")
