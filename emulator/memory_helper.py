def get_zero_page_addr(address_in, offset=0):
    return address_in + offset


def get_absolute_addr(address_in_low, address_in_high, offset=0):
    return (address_in_high << 8 | address_in_low) + offset


def convert_8bit_twos(num):
       if (num & (1 << 7)):
           return -((num ^ 0xFF) + 1)
       else:
           return num


def get_relative_addr(PC, address_in):
    offset = convert_8bit_twos(address_in)
    addr = PC + offset
    return addr


def get_indirect_addr(system, address_in, reg_offset=0):
    # import pdb; pdb.set_trace()
    addr = system.loadMem(address_in) + (system.loadMem(address_in + 1) << 8)
    return addr + reg_offset


def get_indirect_addr_x(system, address_in, register_x):
    return get_indirect_addr(system, address_in+register_x)


def page_diff(addr1, addr2):
    return (addr1 & 0xFF00) != (addr2 & 0xFF00)


def get_indirect_addr_y(system, address_in, register_y):
    return get_indirect_addr(system, address_in, register_y)
