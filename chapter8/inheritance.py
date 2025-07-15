class programmer:
    company="Infosys"
    def show(self,salary):
        self.salary=salary
        print(f"The salary of {self.company} is {self.salary}")


class inherit(programmer):
    company="Mittsure"
    def showcase(self,pin):
        self.pin=pin
        print(f"The pin of {self.company} is {self.pin}")


ashish= inherit()
ashish.showcase(230230)
print(ashish.company)

sasuke= programmer()
print(sasuke.company)
sasuke.show(15000)
