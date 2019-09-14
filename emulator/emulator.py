from py import system
from py.operations import *

systemCPU = system.System()

def printSystemStatus():
    return
    print("")


# Read file
with open('./emulator/bin/brk', 'rb') as file:
    rom_bytes = file.read()
    rom_bytes = rom_bytes[5:]
    i = 0
    while i < len(rom_bytes):
        opcode = hex(rom_bytes[i])

        if opcode == '0x0':
            pass
        elif opcode == '0xa0':
            print("LDY abs")
            i = i + 1
        elif opcode == '0xb9':
            print("LDA abs,y")
            i = i + 2
        elif opcode == '0xc8':
            IncreaseReg0xC8()
            print("INY")
        elif opcode == '0xbe':
            print("LDX abs, y")
            i = i + 2
        else:
            pass
            #print(opcode)
            #print("Instrução invalida!")


        i = i + 1
        if (True):
           print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        else:
           print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
