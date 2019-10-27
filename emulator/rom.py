class Rom():
    file = None
    header = None
    prg_rom_size = 0
    chr_rom_size = 0
    prg_rom = None
    chr_rom = None
    interrupt_handlers = {}
    mapper = -1
    mirroring = False

    def __init__(self, filename):
        self.file = open(filename, "rb")

        self.header = self.file.read(16)
        print (self.header)
        if not self.header[:3] == b'NES':
            import pdb; pdb.set_trace()
            raise Exception("Invalid ROM for NES!")

        self.prg_rom_size = self.header[4]

        self.interrupt_handlers = {
            'NMI_HANDLER': 0xFFFA,
            'RESET_HANDLER': 0xFFFC,
            'IRQ_HANDLER': 0xFFFE,
            'BRK_HANDLER': 0xFFFE,
        }

        self.chr_rom_size = self.header[5]
        self.prg_rom = self.file.read(self.prg_rom_size * 1024 * 16)
        self.mapper = (self.header[7] & 0xF0) | ((self.header[6] & 0xF0) >> 4)
        self.mirroring = bool(self.header[6] & 0b1)

        try:
            self.chr_rom = self.file.read(self.chr_rom_size * 1024 * 8)
        except:
            self.chr_rom = None
