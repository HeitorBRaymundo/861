import time
from .controllers import *

class System():
    A = 0
    X = 0
    Y = 0
    mem = [0] * 2049
    FLAGS = {"C": 0, "Z": 0, "I": 0, "D": 0, "B": 0, "O": 0, "N": 0}
    stack = []
    rom = None
    PC_OFFSET = 0
    SP_OFFSET = 0
    program_counter = 0
    stack_val_return = 0
    branch_hit = False
    stack_neg = False
    cycle_counter = 0
    _counter = 0
    time = -1
    on_nmi = False
    active_nmi = False
    def __init__ (self, rom):
        System._counter += 1
        self.id = System._counter
        self.A = 0
        self.X = 0
        self.Y = 0
        self.mem = [0] * 2049
        self.FLAGS = {"N": 0, "V": 0, "B": 1, "D": 0, "I": 1, "Z": 0, "C": 0}
        self.stack = [0] * 512
        self.rom = rom
        self.PC_OFFSET = 0x8000 if (self.rom.prg_rom_size==2) else 0xC000
        if 'pacman' in rom.filename:
            self.program_counter = ((self.rom.pgr_rom[self.rom.interrupt_handlers['RESET_HANDLER'] + 1 - self.PC_OFFSET] << 8) +  \
                                    (self.rom.pgr_rom[self.rom.interrupt_handlers['RESET_HANDLER'] - self.PC_OFFSET])) -          \
                                     0x8000
        else:
            self.program_counter = ((self.rom.pgr_rom[self.rom.interrupt_handlers['RESET_HANDLER'] + 1 - self.PC_OFFSET] << 8) +  \
                                    (self.rom.pgr_rom[self.rom.interrupt_handlers['RESET_HANDLER'] - self.PC_OFFSET])) -          \
                                     self.PC_OFFSET                                     

        # print("-----------------------------------------------------------")
        # print("INITIAL PC: ", hex(self.program_counter))
        # print("-----------------------------------------------------------")
        self.stack_pointer = 0x01fd
        self.stack_val_return = 0
        self.branch_hit = False
        self.stack_neg = False
        self.ppu_set = 0
        self.time = -1
        self.cycle_counter = 0
        self.on_nmi = False
        self.active_nmi = False
        self.player1_key_index = 0
        self.player2_key_index = 0
        self.all_keys = []
        self.batatinha = [0] * 0x10000
        self.address2006 = 0
        self.address2006Hi = -1
        self.address2006Lo = 0
        self.flag_increment_mode = 0
        self.contadorLixo = 0
        self.mem[0x200:0x300] = rom.pgr_rom[0x2020:0x2120]
        self.address2003 = -1
        self.vblank = 1
        self.sprite_0 = 0
        self.spr_over = 0
        
        # ppu flags register 2001
        self.emphasis_blue = 0
        self.emphasis_green = 0
        self.emphasis_red = 0
        self.enable_sprite = 1
        self.enable_bg = 1
        self.enable_left_column = 0
        self.enable_left_bg_column = 0
        self.greyscale = 0


    def getA(self):
        return self.A

    def setA(self, newA):
        self.A = newA % 256

    def getX(self):
        return self.X

    def setX(self, newX):
        self.X = newX % 256

    def getY(self):
        return self.Y

    def setY(self, newY):
        self.Y = newY % 256

    def getFLAG(self, flag = 0):
        if (flag):
            return self.FLAGS[flag]

        return "{}{}{}{}{}{}{}".format(self.FLAGS["N"], self.FLAGS["V"], self.FLAGS["B"], self.FLAGS["D"], self.FLAGS["I"], self.FLAGS["Z"], self.FLAGS["C"],)

    def printFLAG(self, flag = 0):
        if (flag):
            return self.FLAGS[flag]

        return "{}{}1{}{}{}{}{}".format(self.FLAGS["N"], self.FLAGS["V"], self.FLAGS["B"], self.FLAGS["D"], self.FLAGS["I"], self.FLAGS["Z"], self.FLAGS["C"],)

    def setFLAG(self, flag, newValue):
        self.FLAGS[flag] = newValue

    def stack_push(self, value, numBytes):
        if numBytes == 2:
            if value < 0:
                self.stack_neg = True

            hi, lo = (value & 0xffff).to_bytes(2, 'big')
            self.stack[self.stack_pointer] = hi
            self.stack[self.stack_pointer - 1] = lo
            self.stack_pointer = self.stack_pointer - 2
        else:
            self.stack[self.stack_pointer] = value
            self.stack_pointer = self.stack_pointer - 1

    def stack_pop(self):
        if len(self.stack) <= 0:
            raise Exception("Stack is empty!")
        else:
            self.stack_pointer = self.stack_pointer + 1
            return self.stack[self.stack_pointer]

    # Problema com a stack:
    # Valor que o SP anda depende do número de bytes lido ou salvo na pilha
    # Ideia de refactor: mudar a push para quebrar o valor que será guardado em bytes e salvar byte a byte na pilha
    # pop continua desempilhando 1 byte só e se precisarmos de mais, chamamos a pop mais de uma vez
    def getSP(self):
        return hex(self.stack_pointer) # com refactor não precisa desse 2 multiplicando (tamanho da pilha fica em bytes)

    def setMem(self, address, value):
        if address < 0x2000:
            try:
                # map the addres between 0 to 0x0800
                if type(address) == str:
                    converted_address = int(address, 16) & int('0x7ff', 16)
                else:
                    converted_address = int(address) & int('0x7ff', 16)
            except:
                raise Exception('Invalid type of address!')
            try:
                # save the value
                self.mem[converted_address] = value
            except:
                # import pdb;pdb.set_trace()
                raise Exception("Invalid address!")
        elif address == 0x2000:
            self.flag_name_table =  0x2000 + (0x400 * value % 4)
            self.flag_increment_mode = 32 if ((value >> 2) % 2) else 1
            self.flag_tile_select = (value >> 3) % 2
            self.flag_bg_tile = (value >> 4) % 2
            self.flag_sprite_height = (8,16) if((value >> 5) % 2) else (8,8)
            self.flag_PPU_master_slave = (value >> 6) % 2
            self.active_nmi = (value & 0b10000000) > 0
        elif address == 0x2001:
            # print ("0b",bin(value)[2:].zfill(8))
            self.greyscale = 1 if (value % 2) else 0
            self.enable_left_bg_column = 1 if ((value >> 1) % 2) else 0
            self.enable_left_column = 1 if ((value >> 2) % 2) else 0
            self.enable_bg = 1 if ((value >> 3) % 2) else 0
            self.enable_sprite = 1 if ((value >> 4) % 2) else 0
            self.emphasis_red = 1 if ((value >> 5) % 2) else 0
            self.emphasis_green = 1 if ((value >> 6) % 2) else 0
            self.emphasis_blue = 1 if ((value >> 7) % 2) else 0
        elif address == 0x2003:
            self.address2003 = value
        elif address == 0x2004:
            self.batatinha[self.address2003] = value
            self.address2003 = (self.address2003 + 1) & 0xFF
        else:
            if(address == 0x2006):
                if (self.address2006Hi == -1):
                    self.address2006Hi = value
                    self.address2006 = (self.address2006Hi & 0xff) << 8
                    # print ("Comocaremos novo store or not", hex(self.address2006))
                else:
                    self.address2006 = ((self.address2006Hi & 0xff) << 8) + (value & 0xff)
                    # print ("Novo store oriundo de High:", hex(self.address2006Hi), " e Low: ", hex(value), " virando: ", hex(self.address2006))
                    self.address2006Hi = -1
            elif (address == 0x2007):
                if (self.address2006 >= 0x2000 and self.address2006 < 0x3000):
                    # print(hex(self.address2006), value)
                    self.batatinha[self.address2006 + 0x800] = value
                    self.batatinha[self.address2006] = value
                elif self.address2006 < 0x3F00: 
                    self.address2006 = self.address2006 % 0x3000
                    self.batatinha[self.address2006] = value
                    # self.batatinha[self.address2006 + 0x800] = value
                elif self.address2006 >= 0x3F20 and self.address2006 < 0x4000:
                    self.batatinha[self.address2006 % 0x3F20] = value
                else:
                    self.batatinha[(self.address2006)%0x4000] = value
                
                # print (hex(self.address2006), value)
                # print (hex(self.address2006), " 2007: ",value)
                self.address2006 = self.address2006 + self.flag_increment_mode
                # print ("prox: ", hex(self.address2006))
            else:
                pass
                # print (hex(address), value)


    def loadMem(self, address):
        # print(hex(address))
        if address < 0x2000:            
            try:
                # map the addres between 0 to 0x0800
                if type(address) == str:
                    converted_address = int(address, 16) & int('0x7ff', 16)
                else:
                    converted_address = int(address) & int('0x7ff', 16)
            except:
                raise Exception('Invalid type of address!')

            return self.mem[converted_address]
        elif address == 0x2002:
            
            value = 0
            value |= self.vblank
            value <<= 1
            value |= self.sprite_0
            value <<= 1
            value |= self.spr_over
            value <<= 5
            self.vblank = 1

            return value
        # elif address <= 0x4000:
        #     print("hey")
        elif address == 16406:
            temp = get_key(self.all_keys, self.player1_key_index, 1)
            if self.player1_key_index != 7:
                self.player1_key_index += 1
            else:
                self.player1_key_index = 0

            return temp
        elif address == 16407:
            temp = get_key(self.all_keys, self.player2_key_index, 2)
            if self.player2_key_index != 7:
                self.player2_key_index += 1
            else:
                self.player2_key_index = 0
            return temp

        elif address >= 0x8000:
            return self.rom.pgr_rom[address - self.PC_OFFSET]
        
if __name__ == '__main__':
    system = System()
