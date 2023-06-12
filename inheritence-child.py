# inheritance means inherit all properties from parent to child class
from OppsDemo import Calculator


class childImpl(Calculator): # --> thorough this parent class "Calculator" is successfully inherited to childImpl class
    num2 = 200

    def __init__(self): # note : if u inherit from from parent calss then check if any constructor is created in parent class
        Calculator.__init__(self, 2, 10) # here calling parent constructor

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()
obj = childImpl()
print(obj.getCompleteData())