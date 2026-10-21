
class ShopClass:
    def __init__(self,snm,onm,ct,ty):
        print(f"Constructor is runningfor shop type : {ty}")
        self.shop_name = snm
        self.owner_name = onm
        self.city = ct
        self.shop_type = ty

sp1 = ShopClass("Charbhuja Medical","Rahul Sharma","pune","Medical")

print(sp1.shop_name)
print(sp1.owner_name)
print(sp1.city)
print(sp1.shop_type)

sp2 = ShopClass("Vishal General Store","Amit Trivedi","latur","Grocery")

print(sp2.shop_name)
print(sp2.owner_name)
print(sp2.city)
print(sp2.shop_type)