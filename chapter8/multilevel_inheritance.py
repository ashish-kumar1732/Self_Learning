class inherit:
    company="gulgule"
    def showcase(self,pin):
        self.pin=pin
        print(f"The pin of {self.company} is {self.pin}")

class programmer(inherit):
    company="Infosys"
    def show(self,salary):
        self.salary=salary
        print(f"The salary of {self.company} is {self.salary}")

class coding(programmer):
    def book(self, price):
        self.price=price
        print(f"{self.price} is the price of the book")


ashish= coding()
ashish.showcase(230230)

ashish.book(200)
print(ashish.company) ### inherit from just parent class