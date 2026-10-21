
class MobileClass:

    def __init__(self,b,m,c,p):
        print(f"Constructor is runningfor mobile brand : {b}")
        self.brand = b
        self.model = m
        self.color = c
        self.price = p

mb1 = MobileClass("Samsung","Galaxy A15","Black",15000)

print(mb1.brand)
print(mb1.model)
print(mb1.color)
print(mb1.price)

mb2 = MobileClass("Vivo","Y28","Blue",18000)

print(mb2.brand)
print(mb2.model)
print(mb2.color)
print(mb2.price)