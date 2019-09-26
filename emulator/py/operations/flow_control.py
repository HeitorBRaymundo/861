####################################
#  JUMP / BRANCH / RETURN / BREAK  #
####################################

from py.system import *

class BRK0x00():
    def __init__(self, system):
        # Force Break
        # interrupt,                       N Z C I D V
        # push PC+2, push SR               - - - 1 - -
        print("BRK impl")

class BPL0x10():
    def __init__(self, system, mem_position):
        # Branch on Result Plus
        # branch on N = 0
        if (system.getFLAG("N") == 0):
            branch()
        print("BPL rel")

class JSR0x20():
    def __init__(self, system, mem_position):
        # Jump to New Location Saving Return Address
        # push (PC+2),                     N Z C I D V
        # (PC+1) -> PCL                    - - - - - -
        # (PC+2) -> PCH
        print("JSR abs")

class BMI0x30():
    def __init__(self, system, mem_position):
        # Branch on Result Minus
        # branch on N = 1
        if (system.getFLAG("N") == 1):
            branch()
        print("BMI rel")

class BVC0x50():
    def __init__(self, system, mem_position):
        # Branch on Overflow Clear
        # branch on V = 0
        if (system.getFLAG("V") == 0):
            branch()
        print("BVC rel")

class RTS0x60():
    def __init__(self, system):
        # Return from Subroutine
        # pull PC, PC+1 -> PC
        print("RTS impl")

class BVS0x70():
    def __init__(self, system, mem_position):
        # Branch on Overflow Set
        # branch on V = 1
        if (system.getFLAG("V") == 1):
            branch()
        print("BVS rel")

class BCC0x90():
    def __init__(self, system, mem_position):
        # Branch on Carry Clear
        # branch on C = 0
        if (system.getFLAG("C") == 0):
            branch()
        print("BCC rel")

class BCS0xB0():
    def __init__(self, system, mem_position):
        # Branch on Carry Set
        # branch on C = 1
        if (system.getFLAG("C") == 1):
            branch()
        print("BCS rel")

class BNE0xD0():
    def __init__(self, system, mem_position):
        # Branch on Result not Zero
        # branch on Z = 0
        if (system.getFLAG("Z") == 0):
            branch()
        print("BNE rel")

class BEQ0xF0():
    def __init__(self, system, mem_position):
        # Branch on Result Zero
        # branch on Z = 1
        print("mem_position: ", mem_position)
        print("mem_position bin: ", '{0:08b}'.format(mem_position))
        comp_2 = (~mem_position)
        print("comp_2: ", '{0:08b}'.format(comp_2))
        if (system.getFLAG("Z") == 1):
            branch()
        print("BEQ rel")

class JMP_abs0x4C():
    def __init__(self, system, mem_position):
        # Jump to New Location
        # (PC+1) -> PCL
        # (PC+2) -> PCH
        print("JMP abs")

class JMP_ind0x6C():
    def __init__(self, system, mem_position):
        print("JMP ind")

# OK
class SEI0x78():
    def __init__(self, system):
        # Set Interrupt Disable Status
        # 1 -> I
        system.setFLAG("I", 1)
        # print("SEI impl")
