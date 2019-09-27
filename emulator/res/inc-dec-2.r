<<<<<<< HEAD
| pc = 0xC002  | a = 0x20 | x = 0x00 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC003  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC005  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x20 |
| pc = 0xC007  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC009  | a = 0x21 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x21 |
| pc = 0xC00B  | a = 0x21 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC00D  | a = 0x21 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC00F  | a = 0x21 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC011  | a = 0x21 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC013  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x1D |
| pc = 0xC015  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC017  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC019  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC01B  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC01D  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC01F  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC021  | a = 0x1D | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC023  | a = 0x24 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x24 |
=======
| pc = 0xc002  | a = 0x20 | x = 0x00 | y = 0x00 | sp = 0x01ff | p[NV-BDIZC] =  0000000 |
| pc = 0xc003  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01ff | p[NV-BDIZC] =  0000000 |
| pc = 0xc005  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01ff | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x20 |
Traceback (most recent call last):
  File "./emulator/emulator.py", line 164, in <module>
    INC_zero_page_X_0xF6(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
  File "/Users/Heitor/Documents/Unicamp/861/emulator/py/operations/memory.py", line 75, in __init__
    super().__init__(SystemCPU, zpg_index + X)
NameError: name 'zpg_index' is not defined
>>>>>>> d51c9dbe7bfe7152c8553a9efaf2339acb2714ee
