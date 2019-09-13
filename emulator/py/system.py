class System():
    A = 0
    X = 0
    Y = 0
    MEM = [0] * 255
    FLAGS = {"C": 0, "Z": 0, "I": 0, "D": 0, "B": 0, "O": 0, "N": 0}
    SP = 0

    def ___init__ (self):
        self.A = 0
        self.X = 0
        self.Y = 0
        self.MEM = [0] * 255
        self.FLAGS = {"C": 0, "Z": 0, "I": 0, "D": 0, "B": 0, "O": 0, "N": 0}
        self.SP = 0

    def getA(self):
        return self.A

    def setA(self, newA):
        self.A = newA

    def getX(self):
        return self.X

    def setX(self, newX):
        self.X = newX

    def getY(self):
        return self.Y

    def setY(self, newY):
        self.Y = newY

    def getMEM(self, pos, index = 0):
        return self.MEM[pos + index]

    def setMEM(self, pos, newValue, index = 0):
        self.MEM[pos + index] = newValue

    def getFLAG(self, flag = 0):
        if (flag):
            return self.FLAGS[flag]
        return self.FLAGS

    def setFLAG(self, flag, newValue):
        self.FLAGS[flag] = newValue
