class Calculator():

    def __init__(self, number, number2):
        self.number = number
        self.number2 = number2



    def add(self):
        result = self.number + self.number2
        print(result)

    def multiple(self):
        result = self.number * self.number2
        print(result)

    def divide(self):
        if self.number2 != 0:
            result = self.number / self.number2
            print(result)
        else:
            print("Dzielisz przez zero")


test = Calculator(2,4)

test.add()
test.multiple()
test.divide()