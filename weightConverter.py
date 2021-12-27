class WightConverter:

    def ConvertKgToLb(self, Kg):
        Lb = Kg * 2.2
        return Lb
    def ConvertLbToKg(self, Lb):
        Kg = Lb / 2.2
        return Kg

wc = WightConverter()


input1 = input("Do you wanna convert from kg or lb?")
input2 = input("Enter your number:")
input2 = float(input2)
if input1 == "kg":
    y = wc.ConvertKgToLb(input2)
    print("{:.2f}".format(y) + " Lb")

else:
    z = wc.ConvertLbToKg(input2)
    print("{:.2f}".format(z) + " Kg")

