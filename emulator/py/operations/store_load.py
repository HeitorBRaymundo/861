int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

class Store_Op():

    def __init__(self, register, position, system):
        self.register = register
        self.position = position
        self.system = system

    def execute(self):
        try:
            register_value = eval('self.system.' + self.register)
        except:
            raise Exception('Invalid register!')

        self.system.setMem(self.position, register_value)

        return True


# STA
class StoreInA0x81(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x85(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x8D(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x91(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x95(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x99(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInA0x9D(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


# STX
class StoreInX0x86(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInX0x8E(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInX0x96(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


# STY
class StoreInY0x84(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInX0x8C(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class StoreInX0x94(Store_Op):
    def __init__(self, register, address, system):
        super().__init__(register, address, system)
        super().execute()


class Load_Op():
    def __init__(self, register, position, system, value=None):
        self.register = register
        self.position = position
        self.system = system
        self.value = value

    def execute(self):
        # get the value to be loaded
        if not self.value is None:
            value_to_load = self.value
        else:
            try:
                value_to_load = self.system.loadMem(self.position)
            except:
                raise Exception('Invalid number from memory!')

        # set zero flag
        if value_to_load == 0:
            self.system.setFLAG('Z', 1)
        else:
            self.system.setFLAG('Z', 0)

        # if self.register == 'A':
            # set negative flag
        self.system.FLAGS["N"] = int_to_bit(value_to_load)[0]

        # put the value into the register
        try:
            value_to_load = str(value_to_load)
            exec('self.system.' + self.register + '=' + value_to_load)
        except:
            raise Exception('Invalid register to load!')

        return True

class LoadFromA0xA1(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromA0xA5(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()

class LoadFromA0xA9(Load_Op):
    def __init__(self,register, position, system, value):
        super().__init__(register, position, system, value)
        super().execute()

class LoadInA0xAD(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()

class LoadFromA0xB1(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()

class LoadFromA0xB5(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromA0xB9(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadInA0xBD(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromX0xA2(Load_Op):
    def __init__(self,register, position, system, value):
        super().__init__(register, position, system, value)
        super().execute()


class LoadFromX0xA6(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromX0xB6(Load_Op):
    def __init__(self, register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromX0xAE(Load_Op):
    def __init__(self, register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromX0xBE(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromY0xA0(Load_Op):
    def __init__(self, register, position, system, value):
        super().__init__(register, position, system, value)
        super().execute()


class LoadFromY0xA4(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromY0xAC(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromY0xB4(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()


class LoadFromY0xBC(Load_Op):
    def __init__(self,register, position, system):
        super().__init__(register, position, system)
        super().execute()
