class Rom():
    file = None
    header = None
    prg_rom_size = 0
    chr_rom_size = 0
    prg_rom = None
    chr_rom = None

    def __init__(self, filename):
        self.file = open(filename, "rb")

        self.header = self.file.read(16)

        if not self.header[:3] == b'NES':
            raise Exception("Invalid ROM for NES!")

        self.prg_rom_size = self.header[4]
        self.chr_rom_size = self.header[5]

        self.prg_rom = self.file.read(self.prg_rom_size * 1024 * 16)

        try:
            self.chr_rom = self.file.read(self.chr_rom_size * 1024 * 8)
        except:
            self.chr_rom = None
