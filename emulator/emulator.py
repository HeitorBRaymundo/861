import sys
from py import system
from py.operations import *
from rom import Rom
from memory_helper import *
from threading import Timer,Thread,Event
import time
import ppu

cycle_counter = 0
stop_threads = False

class MyThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

        self.cycle_counter = 0
        self.last_timestamp = time.time()
        print("Cycles: ", self.cycle_counter)
        print("Time Elapsed: ", time.time() - self.last_timestamp)

    def run(self):
        while not self.stopped.wait(0.00000000000000001):
            if self.cycle_counter >= 60:
                print("Cycles: ", self.cycle_counter)
                print("Time Elapsed: ", time.time() - self.last_timestamp)
                self.cycle_counter = 0
                self.last_timestamp = time.time()
            else:
                pass

try:
    file = sys.argv[1]
except:
    pass

print ("A")
nesROM = Rom(file)
systemCPU = system.System(nesROM)

pgr_bytes = nesROM.prg_rom
chr_rom = nesROM.chr_rom
chr_size = nesROM.chr_rom_size * 8 * 1024


stopFlag = Event()
thread = MyThread(stopFlag)
thread.start()


i = 0
m = 0
# print (hex(chr_rom[1]))

spriteList = []
posSprite = []

while i < chr_size:

    flag = False
    lowList = []
    highList = []
    
    j = 0
    while j < 8:
        try:
            temporary = hex(chr_rom[i + j])
        except:
            flag = False
            break
        temporary2 = bin(chr_rom[i + j])[2:].zfill(8)
        lowList.append(temporary2)
        if (temporary != '0xff'):
            flag = True
        # print (i + j, " ", temporary2)
        j = j + 1

    i = i + 8
    
    if (flag):
        j = 0
        flag = False
        while j < 8:
            try:
                temporary = hex(chr_rom[i + j])
            except:
                flag = False
                break
            temporary2 = bin(chr_rom[i + j])[2:].zfill(8)
            # print (temporary2)
            highList.append(temporary2)
            if (temporary != '0xff'):
                flag = True
            j = j + 1
        if (flag):
            i = i + 8
            colorList = []
            for k in range(8):
                for l in range(8):
                    colorList.append(int(lowList[k][l]) + 2 * int(highList[k][l]))
            spriteList.append(colorList)
            m = m + 1
    # i = i + 1

for i in range(len(spriteList)):
    print (i)
    print (spriteList[i])
    

print ("Num sprite: ", m)

positionConfigSprite = 0xe000

# 32 por conta do upload das cores do pallet
i = positionConfigSprite - systemCPU.PC_OFFSET
begin = positionConfigSprite - systemCPU.PC_OFFSET
maxSprite = i + 256

k = 0

while i < maxSprite:
    print(hex(pgr_bytes[i]), " i = ", i , " k = ", k)
    i = i + 1
    k = k + 1

i = begin
k = 0

spriteList = spriteList[1:]

# pulo de 32 pois eh o upload dos pallets
a = []
b = 64
array_flag = []
while i < maxSprite:
    # print (hex(pgr_bytes[i]), " ", k)   
    if (k == 33 + b or k == 37 + b or k == 41 + b or k == 45 + b):
        newList = []
        # print ("-------------")
        # print (i)
        # print (pgr_bytes[i])
        # print(spriteList[pgr_bytes[i]])
        # print ("-------------")
        for j in spriteList[pgr_bytes[i]]:
            # newList.append(pgr_bytes[begin + 16 + 4 * pgr_bytes[i + 1] + j])
            # print (bin(pgr_bytes[begin + 16 + 4 * pgr_bytes[i + 1] + j]))
            # print (" - --------- - ")
            newList.append(bin(pgr_bytes[begin + 16 + 4 * pgr_bytes[i + 1] + j])[2:].zfill(8))
        
        if (pgr_bytes[i + 1] >= 64 and pgr_bytes[i + 1] < 128):
            array_flag.append(True)
        else:
            array_flag.append(False)
        posSprite.append([pgr_bytes[i - 1], pgr_bytes[i + 2]])
        a.append(newList)
        # print (posSprite)
        print (newList)
    i = i + 1
    k = k + 1

print (array_flag)

print (a[0])
print (len(a[0]))
# ppu_teste = ppu.PPU()
array_flag = [array_flag[1], array_flag[0], array_flag[3], array_flag[2]]
ppu.teste(a[1], a[0], a[2], a[2], array_flag)

sys.exit()

while systemCPU.program_counter < len(pgr_bytes) - 6:
    opcode = hex(pgr_bytes[systemCPU.program_counter])
    addr = None
    stack = None
    # print (opcode)
    # import pdb; pdb.set_trace()

    if opcode == '0x0':
        systemCPU.program_counter = systemCPU.program_counter + 1
        stop_threads = True
        # this will stop the timer
        stopFlag.set()
        break

    elif opcode == '0x6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        ASL_zero_page_0x06(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ASL_A_0x0A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_absolute_0x0E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x16':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ASL_zero_page_index_0x16(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x1e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ASL_abs_X_0x01E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x26':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_0x26(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x2a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROL_A_0x2A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x2e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_absolute_0x2E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x36':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROL_zero_page_index_0x36(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x3e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROL_abs_X_0x3E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x46':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_0x46(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x4a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        LSR_A_0x4A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_absolute_0x4E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x56':
        systemCPU.program_counter = systemCPU.program_counter + 2
        LSR_zero_page_index_0x56(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x5e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        LSR_abs_X_0x05E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x61':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x61(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x65':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x65(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x66':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_0x66(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0x69':
        systemCPU.program_counter = systemCPU.program_counter + 2
        AddWithCarry0x69(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x6a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        ROR_A_0x6A(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x6d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        AddWithCarry0x6D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x6e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_absolute_0x6E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x71':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x71(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x75':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x75(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x76':
        systemCPU.program_counter = systemCPU.program_counter + 2
        ROR_zero_page_index_0x76(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x79':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        AddWithCarry0x79(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x7d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        AddWithCarry0x7D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x7e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        ROR_abs_X_0x7E(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0x88':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0x88(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xc6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        DEC_zero_page_0xC6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xc8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xC8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xca':
        systemCPU.program_counter = systemCPU.program_counter + 1
        DecreaseReg0xCA(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xce':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        DEC_absolute_0xCE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xd6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_zero_page_X_0xD6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xde':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        DEC_absolute_X_0xDE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 7
    elif opcode == '0xe1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_x(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xE1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xe5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xE5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xe6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        INC_zero_page_0xE6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
    elif opcode == '0xe8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        IncreaseReg0xE8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        SubWithCarry0xE9(systemCPU, pgr_bytes[systemCPU.program_counter - 1])
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xed':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        SubWithCarry0xED(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xee':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        INC_absolute_0xEE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xf1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_indirect_addr_y(systemCPU, pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xf5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xF5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xf6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_zero_page_X_0xF6(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xf9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getY())
        SubWithCarry0xF9(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xfd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        SubWithCarry0xFD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xfe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1], systemCPU.getX())
        INC_absolute_X_0xFE(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 7

    # PAREI AQUI
    # FUSCA \/
    elif opcode == '0x8': # Flags / stack
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHP0x08(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3
        stack_val = systemCPU.stack_val_return
        # i = i + 0
    elif opcode == '0x18':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLC0x18(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x28':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLP0x28(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
        # i = i + 0
    elif opcode == '0x38':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEC0x38(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x48':
        systemCPU.program_counter = systemCPU.program_counter + 1
        stack = systemCPU.stack_pointer
        PHA0x48(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3
        stack_val = systemCPU.stack_val_return
        # i = i + 0
    elif opcode == '0x68':
        systemCPU.program_counter = systemCPU.program_counter + 1
        PLA0x68(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        stack_val = systemCPU.stack_val_return
        stack = systemCPU.stack_pointer
        # i = i + 0
    elif opcode == '0xb8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLV0xB8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xd8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        CLD0xD8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xf8':

        systemCPU.program_counter = systemCPU.program_counter + 1
        SED0xF8(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0x24': # Bit test HELP

        systemCPU.program_counter = systemCPU.program_counter + 2
        addr = get_zero_page_addr(pgr_bytes[systemCPU.program_counter - 1])
        BIT_zpg0x24(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
        # i = i + 1
    elif opcode == '0x2c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        addr = get_absolute_addr(pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
        BIT_abs0x2C(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        # i = i + 2
    elif opcode == '0x40': # interrupt
        systemCPU.program_counter = systemCPU.program_counter + 1
        RTI0x40(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6
        # i = i + 0
    elif opcode == '0x58':
        systemCPU.program_counter = systemCPU.program_counter + 1
        CLI0x58(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
        # i = i + 0
    elif opcode == '0xea': # NOP
        systemCPU.program_counter = systemCPU.program_counter + 1
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x10':
        systemCPU.program_counter = systemCPU.program_counter + 2
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        old_pc = systemCPU.program_counter
        BPL0x10(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0x20':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.stack_push(systemCPU.program_counter, 2)
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        thread.cycle_counter = thread.cycle_counter + 6
        # i = i + 1
    elif opcode == '0x30':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BMI0x30(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x50':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVC0x50(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x60':
        lo = systemCPU.stack_pop()
        hi = systemCPU.stack_pop()
        hi = hi << 8

        if systemCPU.stack_neg:
            systemCPU.program_counter = - (((hi | lo) ^ 0xfff) + 1)
        else:
            systemCPU.program_counter = hi | lo
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x6c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        low = pgr_bytes[systemCPU.program_counter - 2]
        high = pgr_bytes[systemCPU.program_counter - 1]
        systemCPU.program_counter = get_absolute_addr(low, high) - 0xC000
        thread.cycle_counter = thread.cycle_counter + 5

    elif opcode == '0x70':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BVS0x70(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x78':
        systemCPU.program_counter = systemCPU.program_counter + 1
        SEI0x78(systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x90':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCC0x90(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xb0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BCS0xB0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xd0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BNE0xD0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xf0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        old_pc = systemCPU.program_counter
        setPCToAddress = get_relative_addr(systemCPU.program_counter, pgr_bytes[systemCPU.program_counter - 1])
        BEQ0xF0(systemCPU, setPCToAddress)
        thread.cycle_counter = thread.cycle_counter + 2
        if systemCPU.branch_hit:
            thread.cycle_counter = thread.cycle_counter + 1
        if page_diff(old_pc, systemCPU.program_counter):
            thread.cycle_counter = thread.cycle_counter + 2
    # HEITOR \/
    elif opcode == '0x1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        OrWithAcumulator0x01(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        OrWithAcumulator0x05(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        OrWithAcumulator0x09(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        OrWithAcumulator0x0D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x11':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        OrWithAcumulator0x11(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x15':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        OrWithAcumulator0x15(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x19':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x19(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x1d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        OrWithAcumulator0x1D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x21':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        AndWithAcumulator0x21(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x25':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        AndWithAcumulator0x25(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x29':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        AndWithAcumulator0x29(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x2d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        AndWithAcumulator0x2D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x31':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        AndWithAcumulator0x31(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x35':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        AndWithAcumulator0x35(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x39':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x39(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x3d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        AndWithAcumulator0x3D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x41':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        ExclusiveOrWithAcumulator0x41(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0x45':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        ExclusiveOrWithAcumulator0x45(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0x49':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        ExclusiveOrWithAcumulator0x49(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x4d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        ExclusiveOrWithAcumulator0x4D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x51':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        ExclusiveOrWithAcumulator0x51(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x55':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        ExclusiveOrWithAcumulator0x55(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0x59':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x59(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0x5d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        ExclusiveOrWithAcumulator0x5D(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xc0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithY0xC0(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xc1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_x(systemCPU, operand, systemCPU.X)
        CompareWithAcumulator0xC1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 6
    elif opcode == '0xc4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithY0xC4(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xc5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithAcumulator0xC5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xc9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithAcumulator0xC9(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xcc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithY0xCC(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xcd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithAcumulator0xCD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xd1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_indirect_addr_y(systemCPU, operand, systemCPU.Y)
        CompareWithAcumulator0xD1(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xd5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        CompareWithAcumulator0xD5(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
    elif opcode == '0xd9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xD9(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xdd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        CompareWithAcumulator0xDD(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xe0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        CompareWithX0xE0(systemCPU, operand)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xe4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        CompareWithX0xE4(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 3
    elif opcode == '0xec':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        CompareWithX0xEC(systemCPU, addr)
        thread.cycle_counter = thread.cycle_counter + 4

    # CARTS \/
    # STORES
    elif opcode == '0x81':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        StoreInA0x81(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0x84':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x85':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInY0x84(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x86':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        StoreInX0x86(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0x8c':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8C(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x8d':
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInA0x8D(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x8e':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        StoreInX0x8E(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x91':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        StoreInA0x91(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0x94':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x94(register='Y', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x95':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        StoreInA0x95(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x96':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        StoreInX0x96(register='X', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0x99':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x99(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5


    elif opcode == '0x9d':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        StoreInA0x9D(register='A', address=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5


    # LOADS
    elif opcode == '0xa0':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromY0xA0(register='Y', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xa1':
        # import pdb; pdb.set_trace()
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_indirect_addr_x(systemCPU, operand, offset)
        LoadFromA0xA1(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 6

    elif opcode == '0xa2':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromX0xA2(register='X', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xa4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromY0xA4(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromA0xA5(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_zero_page_addr(operand)
        LoadFromX0xA6(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 3

    elif opcode == '0xa9':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        LoadFromA0xA9(register='A', position=-1, system=systemCPU, value=operand)
        thread.cycle_counter = thread.cycle_counter + 2

    elif opcode == '0xac':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromY0xAC(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xad':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadInA0xAD(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xae':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        addr = get_absolute_addr(operand_low, operand_high)
        LoadFromX0xAE(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb1':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_indirect_addr_y(systemCPU, operand, offset)
        LoadFromA0xB1(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 5
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xb4':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromY0xB4(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb5':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_zero_page_addr(operand, offset)
        LoadFromA0xB5(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb6':
        systemCPU.program_counter = systemCPU.program_counter + 2
        operand = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_zero_page_addr(operand, offset)
        LoadFromX0xB6(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4

    elif opcode == '0xb9':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromA0xB9(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbc':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = system.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromY0xBC(register='Y', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbd':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.X
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadInA0xBD(register='A', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getX()):
            thread.cycle_counter = thread.cycle_counter + 1

    elif opcode == '0xbe':
        systemCPU.program_counter = systemCPU.program_counter + 3
        operand_low = pgr_bytes[systemCPU.program_counter - 2]
        operand_high = pgr_bytes[systemCPU.program_counter - 1]
        offset = systemCPU.Y
        addr = get_absolute_addr(operand_low, operand_high, offset)
        LoadFromX0xBE(register='X', position=addr, system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 4
        if page_diff(addr, addr - systemCPU.getY()):
            thread.cycle_counter = thread.cycle_counter + 1


    # TRANSFERS BETWEEN REGISTERS
    elif opcode == '0x8a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TXA_0x8A(first_register='X', second_register='A', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x98':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TYA_0x98(first_register='Y', second_register='A', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xaa':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAX_0xAA(first_register='A', second_register='X', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xa8':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_TAY_0xA8(first_register='A', second_register='Y', system=systemCPU)
        thread.cycle_counter = thread.cycle_counter + 2

    # TRANSFERS TO THE STACK POINTER
    elif opcode == '0x9a':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_X_to_SP_Op_0x9A(system=systemCPU).execute()
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0xba':
        systemCPU.program_counter = systemCPU.program_counter + 1
        Transfer_SP_to_X_Op_0xBA(system=systemCPU).execute()
        thread.cycle_counter = thread.cycle_counter + 2
    elif opcode == '0x':
        systemCPU.program_counter = systemCPU.program_counter + 1
    else:
        print ("Erro")
        pass

    if addr is None and stack is None:
       # print("PC: ", systemCPU.program_counter)
       print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
              "| a = 0x%0.2x" % systemCPU.getA(), "| x = 0x%0.2x" %  systemCPU.getX(), \
              "| y = 0x%0.2x" %  systemCPU.getY(), "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
              "| p[NV-BDIZC] =", systemCPU.printFLAG(),"|")
    elif addr is not None and stack is None:
       print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
              "| a = 0x%0.2x" % systemCPU.getA(), \
              "| x = 0x%0.2x" %  systemCPU.getX(), \
              "| y = 0x%0.2x" %  systemCPU.getY(), \
              "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
              "| p[NV-BDIZC] =", systemCPU.printFLAG(),\
              "| MEM[0x%0.4x]" % addr, "= 0x%0.2x" % systemCPU.loadMem(addr),"|")
    elif addr is None and stack is not None:
       print ("| pc = 0x%0.4x" % int(hex(systemCPU.program_counter + systemCPU.PC_OFFSET), 16),\
              "| a = 0x%0.2x" % systemCPU.getA(), \
              "| x = 0x%0.2x" %  systemCPU.getX(), \
              "| y = 0x%0.2x" %  systemCPU.getY(), \
              "| sp = 0x%0.4x" %  int(systemCPU.getSP(), 16), \
              "| p[NV-BDIZC] =", systemCPU.printFLAG(),\
              "| MEM[0x%0.4x]" % stack, "= 0x%0.2x" % stack_val,"|")
