from Cw03_stachelek.zad5 import Calculator


class ScienceCalculator(Calculator):
    def exponentiation(self):
        number3 = self.number1
        for i in range(1, self.number2):
            number3 *= self.number1
        return number3


calculate = ScienceCalculator(2, 3)
print(calculate.exponentiation())
