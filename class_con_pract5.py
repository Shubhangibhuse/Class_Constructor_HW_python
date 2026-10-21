
class AutoClass:
    def __init__(self,ano,dnm,c):
        print(f"Constructor is runningfor Auto no : {ano}")
        self.Auto_no = ano
        self.driver_name = dnm
        self.color = c

auto1 = AutoClass("MH-12 AB-1234","Sunil Kadam","yellow")

print(auto1.Auto_no)
print(auto1.driver_name)
print(auto1.color)

auto2 = AutoClass("MH-24 AB-1834","Raju Shaikh","Green")

print(auto2.Auto_no)
print(auto2.driver_name)
print(auto2.color)