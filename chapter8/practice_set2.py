###### 1st Problem #######

# class programmer:

#     company = "MicroSoft"

#     def __init__(self,name,salary,pin,company):
#         self.name= name
#         self.salary=salary
#         self.pin=pin
#         self.company=company

# p = programmer("Ashish",20000,303313,"Google")
# print(p.salary,p.name)
# print(p.company,p.pin)


####### 2nd Problem #########


class calculator:
    def square(self,n):
        self.n=n
        return f"Square of {self.n} is {self.n*self.n}"
    def cube(self,m):
        self.m=m
        return f"Cube of {self.m} is {self.m*self.m*self.m}"
    def square_root(self,k):
        self.k=k
        return f"square root of {self.k} is {self.k**0.5}"



