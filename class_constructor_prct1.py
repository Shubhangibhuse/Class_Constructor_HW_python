
class Bus:

    def __init__(self,nm,no,c,r):
        print(f"Constructor is runningfor bus name : {nm}")
        self.bus_name = nm
        self.bus_no = no
        self.bus_color = c
        self.route = r

obj1 = Bus("Shivshahi",204,"White","pune to latur")

print(obj1.bus_name)
print(obj1.bus_no)
print(obj1.bus_color)
print(obj1.route)

obj2= Bus("Shivneri",101,"Blue","pune to mumbai")

print(obj2.bus_name)
print(obj2.bus_no)
print(obj2.bus_color)
print(obj2.route)

