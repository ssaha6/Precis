from z3 import *

class PrecisVar:
    def __init__(self, varName, varType, isNew):
        # Check variable type
        self.checkVarType(varType)

        self.varName = varName
        self.isNew = isNew

        if varType.upper() == 'INT':
            self.varZ3 = Int(varName)
        elif varType.upper() == 'FLOAT':
            self.varZ3 = Real(varName)
        elif varType.upper() == 'BOOL':
            self.varZ3 = Bool(varName)
        else:
            print('Unknown type!')
            exit(1)

    # DEBUG method
    def checkVarType(self, varType):
        assert(varType.upper() == 'INT' or varType.upper() == 'FLOAT' or varType.upper() == 'BOOL')
    
if __name__ == '__main__':
    print(0)
