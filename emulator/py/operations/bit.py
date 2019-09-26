################################
#        BIT OPERATIONS        #
################################

from py.system import *

class BIT_zpg0x24():
    def __init__(self, zpg: int, A: int, SR: int):
        # bits 7 and 6 of operand are transfered to bit 7 and 6 of SR (N,V);
        # the zeroflag is set to the result of operand AND accumulator.
        print("BIT zpg")

class BIT_abs0x2C():
    def __init__(self, absolute: int, A: int, SR: int):
        print("BIT abs")
