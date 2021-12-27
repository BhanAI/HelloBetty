import random

class LotteryGenerator:

    numbers = []

    def gerRandomNumber(self):
        return random.randint(1, 49)

    def getFinalNumbers(self):
        i = 0
        while i < 7:
            y = self.gerRandomNumber()
            if y not in self.numbers:
                self.numbers.append(y)
                i += 1
        return self.numbers


lotteryGenerator = LotteryGenerator()
n = lotteryGenerator.getFinalNumbers()
print(n)
