
class HouseClass:
    def __init__(self,hn,onm,c,add):
        print(f"Constructor is runningfor House no : {hn}")
        self.house_no = hn
        self.owner_name = onm
        self.house_color = c
        self.address = add

hs1 = HouseClass(502,"Shubhangi Bhuse","White","Latur")

print(hs1.house_no)
print(hs1.owner_name)
print(hs1.house_color)
print(hs1.address)

hs2 = HouseClass(505,"Narsing Bhuse","Yellow","Pune")

print(hs2.house_no)
print(hs2.owner_name)
print(hs2.house_color)
print(hs2.address)