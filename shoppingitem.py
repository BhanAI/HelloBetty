class Itemcart:
    cart = {}

    def addToList(self, product, price):
        self.cart[product] = price

    def subTotal(self):
        sumPrice = 0
        for product in self.cart:
            sumPrice += self.cart[product]
        return sumPrice

    def total(self):
        sumPriceTaxIn = self.subTotal() * 1.08
        return sumPriceTaxIn

    def returnList(self):
        return self.cart


c1 = Itemcart()

c1.addToList("laptop", 900)
c1.addToList("phone", 1000)
c1.addToList("headphone", 200)

print("Your items are:", c1.returnList())
print("Your subtotal price is:", c1.subTotal())
print("Your total price with taxes is:", c1.total())