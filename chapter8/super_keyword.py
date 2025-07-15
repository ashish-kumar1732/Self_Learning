class employee:
    def __init__(self):
        print("constructor of employee")

class waiter(employee):
    def __init__(self):
        print("constructor of waiter")
        

class manager(waiter):
    def __init__(self):
        super().__init__() ### super keyword is used to run function of parent class
        print("constructor of manager")

call = manager()
print(call)