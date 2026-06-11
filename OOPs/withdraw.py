class Currency:
    def __init__(self, amount):
        self.amount = amount

    def withdraw(self, amount):
        self.amount -= amount
        return self.amount

    def show(self):
        return self.amount


c = Currency(80)
sum = c.withdraw(20)
print(sum)
