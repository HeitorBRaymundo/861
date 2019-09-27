################################
#        BIT OPERATIONS        #
################################

from py.system import *

int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]


# OK
# tested
class BIT_zpg0x24():
    def __init__(self, system, address):
        # bits 7 and 6 of operand are transfered to bit 7 and 6 of SR (N,V);
        # the zeroflag is set to the result of operand AND accumulator.

        a = system.getA()
        value_in_mem = system.loadMem(address)

        system.setFLAG("N", int_to_bit(value_in_mem)[0])
        system.setFLAG("V", int_to_bit(value_in_mem)[1])

        andResult = a & value_in_mem
        if (andResult == 0):
            system.setFLAG("Z", 1)
        else:
            system.setFLAG("Z", 0)

# OK
# tsted
class BIT_abs0x2C():
    def __init__(self, system, address):

        a = system.getA()
        value_in_mem = system.loadMem(address)

        system.setFLAG("N", int_to_bit(value_in_mem)[0])
        system.setFLAG("V", int_to_bit(value_in_mem)[1])

        andResult = a & value_in_mem
        if (andResult == 0):
            system.setFLAG("Z", 1)
        else:
            system.setFLAG("Z", 0)
