from py import system

system = system.System()

def printSystemStatus():
    return
    print("")


# Read file
with open('bin/brk', 'rb') as file:
    rom_bytes = file.read()

    for i in range(0, len(rom_bytes)):
        opcode = hex(rom_bytes[i])
        # do stuff
        printSystemStatus()
