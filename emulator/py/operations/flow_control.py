####################################
#  JUMP / BRANCH / RETURN / BREAK  #
####################################

from py.system import *

class BRK0x00():
    def __init__(self, system):
        pass
        # Force Break
        # interrupt,                       N Z C I D V
        # push PC+2, push SR               - - - 1 - -
# OK
# tested
class BPL0x10():
    def __init__(self, system, mem_position):
        # Branch on Result Plus
        # branch on N = 0
        if (system.getFLAG("N") == 0):
            system.program_counter = mem_position
# OK
# tested
class JSR0x20():
    def __init__(self, system, mem_position):
        pass
        # Jump to New Location Saving Return Address
        # push (PC+2),                     N Z C I D V
        # (PC+1) -> PCL                    - - - - - -
        # (PC+2) -> PCH

# tested
class BMI0x30():
    def __init__(self, system, mem_position):
        # Branch on Result Minus
        # branch on N = 1
        if (system.getFLAG("N") == 1):
            system.program_counter = mem_position

class BVC0x50():
    def __init__(self, system, mem_position):
        # Branch on Overflow Clear
        # branch on V = 0
        if (system.getFLAG("V") == 0):
            system.program_counter = mem_position

# OK
# tested
class RTS0x60():
    def __init__(self, system):
        pass
        # Return from Subroutine
        # pull PC, PC+1 -> PC

class BVS0x70():
    def __init__(self, system, mem_position):
        # Branch on Overflow Set
        # branch on V = 1
        if (system.getFLAG("V") == 1):
            system.program_counter = mem_position
# tested
class BCC0x90():
    def __init__(self, system, mem_position):
        # Branch on Carry Clear
        # branch on C = 0
        if (system.getFLAG("C") == 0):
            system.program_counter = mem_position
# tested
class BCS0xB0():
    def __init__(self, system, mem_position):
        # Branch on Carry Set
        # branch on C = 1
        if (system.getFLAG("C") == 1):
            system.program_counter = mem_position

# tested
class BNE0xD0():
    def __init__(self, system, mem_position):
        # Branch on Result not Zero
        # branch on Z = 0
        if (system.getFLAG("Z") == 0):
            system.program_counter = mem_position

# OK
class BEQ0xF0():
    def __init__(self, system, mem_position):
        # Branch on Result Zero
        # branch on Z = 1

        if (system.getFLAG("Z") == 1):
            system.program_counter = mem_position

# OK
# tested
class JMP_abs0x4C():
    def __init__(self, system, mem_position):
        pass
        # Jump to New Location
        # (PC+1) -> PCL
        # (PC+2) -> PCH

# OK
class JMP_ind0x6C():
    def __init__(self, system, mem_position):
        pass

# OK
class SEI0x78():
    def __init__(self, system):
        # Set Interrupt Disable Status
        # 1 -> I
        system.setFLAG("I", 1)
