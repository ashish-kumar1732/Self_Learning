# class employee():
#     no_of_person = 15


#     @classmethod
#     def print_details(cls):
#         print("hey this is me")
#         return cls()



# # karan = employee()
# # karan.print_details()
# # employee.print_details()
# karan= employee.print_details()

# print(karan.no_of_person)

#------------------------ Single inheritance ---------------

# class employee:
#     npc = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole


# ashish = employee("ashish",55,"instructor")
# arujn = employee("arjun",45,"student")


# class programmer(employee):
#     def __init__(self, aname, asalary, arole, alanguage):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.language= alanguage

#     def programmers_details(self):
#         return f"Name of the programmer is {self.name}, his salary is {self.salary} do work as {self.role} and know {self.language} languages"

# karan = programmer("karan",60, "programmers", ("python", "cpp"))
# kapil = programmer("kapil",40, "sales", ("python"))

# # print(ashish.salary)
# # print(karan.language)
# # print(karan.npc)

# print(karan.programmers_details())



#------------------------ Multiple inheritance ---------------

# class employee:
#     npc = 8

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole

#     def programmers_details(self):
#         return f"Name of the programmer is {self.name}, his salary is {self.salary} do work as {self.role}"


# class programmer:
#     def __init__(self, aname, agame):
#         self.name = aname
#         self.game = agame

#     def programmers_data(self):
#         return f"Name of the programmer is {self.name}, his sports are {self.game}"



# class coolguy (employee, programmer):
#     language = "c++"

#     def __init__(self, aname, asalary, arole, agame):
#         employee.__init__(self, aname, asalary, arole)
#         programmer.__init__(self, aname, agame)

    

# ashish= coolguy("ashish", 556, "coder", "soccer")
# print(ashish.programmers_details())
# print(ashish.programmers_data())



#------------------------ Multi-Level inheritance ---------------

# class dad:
#     volleyball= 1


# class son(dad):
#     dance = 1

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# class grand_son(son):
#     dance = 6

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# ashish= dad()
# ashi= son()
# ash= grand_son()

# print(ash.volleyball)


# class dad:
#     volleyball= 1


# class son(dad):
#     dance = 1
#     volleyball=2

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# class grand_son(son):
#     dance = 6

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# ashish= dad()
# ashi= son()
# ash= grand_son()

# print(ash.volleyball)
# print(ash.is_dance())


# class electronic_device:
#     pass

# class pocket_gadget:
#     pass

# class phone:
#     pass


#------------------- access specifiers ---------------------


# class dad:
#     volleyball= 5
#     __sing =10


# class son(dad):
#     dance = 1
#     _volleyball=2

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# class grand_son(son):
#     dance = 6

#     def is_dance(self):
#         return f" i dance for {self.dance}"
    

# ashish= dad()
# ashi= son()
# ash= grand_son()

# print(ash.volleyball)
# print(ashi._volleyball)
# print(ash.is_dance())
# print(ash._dad__sing)                                        ## Name mangling


#-------------- Polymorphism ------------


print(5+600)
print("5"+"600")