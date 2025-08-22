class employee():
    no_of_leaves=8

    def print_details(self):
        return f"Name is {self.name}, salary is {self.salary} in class {self.std}"


ashi= employee()
ashish= employee()


ashish.name = "Ashish"
ashish.salary= 4500
ashish.std= 4


ashi.name = "Ashi"
ashi.salary= 450
ashi.std= 2

print(ashish.print_details())
print(ashi.print_details())