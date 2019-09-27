SEC impl
| pc = 0xC001 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0000001 |
CLC impl
| pc = 0xC002 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0000000 |
PHP impl
| pc = 0xC003 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01F7  | p[NV-BDIZC] =  0000000 |
PLP impl
| pc = 0xC004 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0000000 |
| pc = 0xC005 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0001000 |
| pc = 0xC006 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0001000 |
| pc = 0xC007 | a = 0x00 | x = 0x00 | y = 0x00 | sp = 0x01FF  | p[NV-BDIZC] =  0001100 |
PLA impl
Traceback (most recent call last):
  File "./emulator/emulator.py", line 295, in <module>
    PLA0x68(systemCPU)
  File "/Users/luizeduardocartolano/Dropbox/DUDU/Unicamp/IC/MC861/workspace/emulator/py/operations/flags.py", line 76, in __init__
    acumulator = system.stack_pop()
  File "/Users/luizeduardocartolano/Dropbox/DUDU/Unicamp/IC/MC861/workspace/emulator/py/system.py", line 57, in stack_pop
    raise Exception("Stack is empty!")
Exception: Stack is empty!
