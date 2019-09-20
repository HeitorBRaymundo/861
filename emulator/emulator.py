from py import system
from py.operations import *

systemCPU = system.System()

def printSystemStatus():
    return
    print("")


# Read file
with open('./emulator/bin/brk-adc', 'rb') as file:
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
        elif opcode == '0xbe':
            print("LDX abs, y")
            i = i + 2
        elif opcode == '0x06':
            print("ASL zpg")
        elif opcode == '0x0a':
        	print("ASL A")
        elif opcode == '0x0e':
        	print("ASL abs")
        elif opcode == '0x16':
        	print("ASL zpg,X")
        elif opcode == '0x1e':
        	print("ASL abs,X")
        elif opcode == '0x26':
        	print("ROL zpg")
        elif opcode == '0x2a':
        	print("ROL A")
        elif opcode == '0x2e':
        	print("ROL abs")
        elif opcode == '0x36':
        	print("ROL zpg,X")
        elif opcode == '0x3e':
        	print("ROL abs,X")
        elif opcode == '0x46':
        	print("LSR zpg")
        elif opcode == '0x4a':
        	print("LSR A")
        elif opcode == '0x4e':
        	print("LSR abs")
        elif opcode == '0x56':
        	print("LSR zpg,X")
        elif opcode == '0x5e':
        	print("LSR abs,X")
        elif opcode == '0x61':
        	print("ADC X,ind")
        elif opcode == '0x65':
        	print("ADC zpg")
        elif opcode == '0x66':
        	print("ROR zpg")
        elif opcode == '0x69':
            print("ADC #")
            i = i + 1
        elif opcode == '0x6a':
        	print("ROR A")
        elif opcode == '0x6d':
            print("ADC abs")
            i = i + 1
        elif opcode == '0x6e':
        	print("ROR abs")
        elif opcode == '0x71':
        	print("ADC ind,Y")
        elif opcode == '0x75':
        	print("ADC zpg,X")
        elif opcode == '0x76':
        	print("ROR zpg,X")
        elif opcode == '0x79':
            print("ADC abs,Y")
            i = i + 2
        elif opcode == '0x7d':
            print("ADC abs,X")
            i = i + 2
        elif opcode == '0x7e':
        	print("ROR abs,X")
        elif opcode == '0x88':
        	print("DEY impl")
        elif opcode == '0xc6':
        	print("DEC zpg")
        elif opcode == '0xc8':
            IncreaseReg0xC8()
            print("INY impl")
        elif opcode == '0xca':
        	print("DEX impl")
        elif opcode == '0xce':
        	print("DEC abs")
        elif opcode == '0xd6':
        	print("DEC zpg,X")
        elif opcode == '0xde':
        	print("DEC abs,X")
        elif opcode == '0xe1':
        	print("SBC X,ind")
        elif opcode == '0xe5':
        	print("SBC zpg")
        elif opcode == '0xe6':
        	print("INC zpg")
        elif opcode == '0xe8':
        	print("INX impl")
        elif opcode == '0xe9':
        	print("SBC #")
        elif opcode == '0xed':
        	print("SBC abs")
        elif opcode == '0xee':
        	print("INC abs")
        elif opcode == '0xf1':
        	print("SBC ind,Y")
        elif opcode == '0xf5':
        	print("SBC zpg,X")
        elif opcode == '0xf6':
        	print("INC zpg,X")
        elif opcode == '0xf9':
        	print("SBC abs,Y")
        elif opcode == '0xfd':
        	print("SBC abs,X")
        elif opcode == '0xfe':
        	print("INC abs,X")
        else:
            pass
            #print(opcode)
            #print("Instrução invalida!")


        i = i + 1
        # if (True):
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," |")
        # else:
        #    print ("| x = ", systemCPU.getX(), " | y = ", systemCPU.getY(), " | sp = ", systemCPU.getSP(), " | p[NV-BDIZC] = ", systemCPU.getFLAG()," | MEM[{}] = ".format(rom_bytes[i + 1], rom_bytes[i + 2], " |"))
