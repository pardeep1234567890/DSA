# To manage complexity when programs become big. , that's why we use the OOPS
class Mobile:
    # Class is a bluePrint and it have attribues 
    def __init__(self, brand,price):
        self.brand = brand
        self.price = price
    # and (functions or methods)
    def show_details(self):
        print(self.brand)
        print(self.price)

s1 = Mobile("samsung",15000)
s1.show_details()