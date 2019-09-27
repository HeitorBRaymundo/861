################################
#        BIT OPERATIONS        #
################################

from py.system import *

# OK
class BIT_zpg0x24():
    def __init__(self, system, address):
        # bits 7 and 6 of operand are transfered to bit 7 and 6 of SR (N,V);
        # the zeroflag is set to the result of operand AND accumulator.

        a = system.getA()
        value_in_mem = system.loadMem(address)

        bin = '{0:08b}'.format(value_in_mem)

        bit7 = bin[7:8]
        bit6 = bin[6:7]

        system.setFLAG("N", bit7)
        system.setFLAG("V", bit6)

        andResult = a & value_in_mem
        if (andResult == 0):
            system.setFLAG("Z", 1)
        else:
            system.setFLAG("Z", 0)

# OK
class BIT_abs0x2C():
    def __init__(self, system, address):

        a = system.getA()
        value_in_mem = system.loadMem(address)

        bin = '{0:08b}'.format(value_in_mem)

        bit7 = bin[7:8]
        bit6 = bin[6:7]

        system.setFLAG("N", bit7)
        system.setFLAG("V", bit6)

        andResult = a & value_in_mem
        if (andResult == 0):
            system.setFLAG("Z", 1)
        else:
            system.setFLAG("Z", 0)
