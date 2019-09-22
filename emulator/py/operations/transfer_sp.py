int_to_bit = lambda n : [n >> i & 1 for i in range(7,-1,-1)]

class Transfer_X_to_SP_Op_0x9A():
    def __init__(self, operation: str, system):
        self.operation = operation
        self.system = system

    def execute(self):
        print (self.operation)
        # get register x values
        value = system.X
        # set zero flag
        if value == 0:
            system.FLAGS["Z"] = 1
        else:
            system.FLAGS["Z"] = 0
        # set negative flag
        system.FLAGS["N"] = int_to_bit(value)[0]
        # push the value in the stack
        system.stack_push(value)

        return True

class Transfer_SP_to_X_Op_0xBA():
    def __init__(self, operation: str, system):
        self.operation = operation
        self.system = system

    def execute(self):
        print (self.operation)
        # get value from stack
        value = system.stack_pop()
        # set zero flag
        if value == 0:
            system.FLAGS["Z"] = 1
        else:
            system.FLAGS["Z"] = 0
        # set negative flag
        system.FLAGS["N"] = int_to_bit(value)[0]
        # put the value in the X register
        system.X = value

        return True
