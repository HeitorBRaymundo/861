| pc = 0xC002  | a = 0x20 | x = 0x00 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC003  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 |
| pc = 0xC005  | a = 0x20 | x = 0x01 | y = 0x00 | sp = 0x01FF | p[NV-BDIZC] =  0000000 | MEM[0x0041]  = 0x20 |
Traceback (most recent call last):
  File "./emulator/emulator.py", line 164, in <module>
    INC_zero_page_X_0xF6(systemCPU, pgr_bytes[systemCPU.program_counter - 2], pgr_bytes[systemCPU.program_counter - 1])
  File "/home/igoromote/2019s2/861/emulator/py/operations/memory.py", line 75, in __init__
    super().__init__(SystemCPU, zpg_index + X)
NameError: name 'zpg_index' is not defined
