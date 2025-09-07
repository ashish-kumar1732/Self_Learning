# class employee():
#     no_of_leaves=8

    # def print_details(self):
    #     return f"Name is {self.name}, salary is {self.salary} in class {self.std}"


# ashi= employee()
# ashish= employee()


# ashish.name = "Ashish"
# ashish.salary= 4500
# ashish.std= 4


# ashi.name = "Ashi"
# ashi.salary= 450
# ashi.std= 2

# print(ashish.print_details())
# print(ashi.print_details())

#             class student():
#     no_of_leaves= 8


#     def __init__(self, aname, asalary, arole):
#         self.name= aname
#         self.salary= asalary
#         self.role= arole


# ashish=student("ashish", 4500, "monitor")
# rohan=student("rohan", 4000, "cr")

# print(ashish.name)
# print(rohan.role)                                                     


# class employee():
#     no_of_leaves=8

#     def __init__(self, aname, asalary, arole):
#         self.name= aname
#         self.salary= asalary
#         self.role= arole

#     # @classmethod
#     # def change_leaves(cls, newleaves):
#     #     cls.no_of_leaves= newleaves
#     #     # return cls.no_of_leaves

#     @classmethod    
#     def first_str(cls, split_str):
#         param= split_str.split("-")
#         print(param)
#         return cls(param[0], int(param[1]), param[2])

 
# # ashish=employee("ashish", 4500, "monitor")
# # rohan=employee("rohan", 4000, "cr")

# # ashish.change_leaves(55)
# # rohan.change_leaves(60)
# # employee.change_leaves(66)

# karan= employee.first_str("Karan-4800-student")
# # print(rohan.no_of_leaves)
# # print(ashish.no_of_leaves)
# # print(employee.no_of_leaves)
# print(employee.no_of_leaves)

# print(karan.salary)


class class_method():
    no_of_employee = 15

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    
    @classmethod
    def split_words(cls, split_details):
        # pram = split_details.split("-")
        # return cls(pram[0],int(pram[1]), pram[2])
        return cls(*split_details.split("-"))

karan = class_method.split_words("karan-4550-developer")

print(karan.salary)



