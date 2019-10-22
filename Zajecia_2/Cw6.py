from . import Cw5
class ScienceCalculator(Cw5.Calculator):
    def potegowanie(self):
        result = self.number ^ self.number2
        print(result)


test2 = ScienceCalculator(2,6)
