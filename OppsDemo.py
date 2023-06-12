# class are nothing but user-defined blueprint or prototype
# sum , multiplication , addition , constant
# A class will methods , class variable , instance variable,constructor etc
# Objects for your classes
# when functions used inside the class then they are called methods

class Calculator:
    num = 100  # class variable is which is created inside class

    # class variable are constant no matter how many obj are created
    # Default constructor
    def __init__(self, a, b):
        self.firstNumber = a  # instance variable is which is created inside constructor
        self.secondNumber = b
        # variables which we define inside constructor are called instance variable
        print("I am called automatically when object is created")

    def GetData(self):
        print("I am now executing as a method in class")

    def summation(self):  # parameter are mandatory when in methods when defined inside the class
        return self.firstNumber + self.secondNumber + Calculator.num  # or self.num
    # self keyword is mandatory for calling variable names in method


# to call the methods you need to create object for this class
# to create the object you need to come out of the class

# obj is passed as self argument
obj = Calculator(2, 3)  # syntax to create object in python , creating obj is similar to calling function in python
obj.GetData()
print(obj.summation())

obj1 = Calculator(4, 5)
obj1.GetData()
print(obj1.summation())
