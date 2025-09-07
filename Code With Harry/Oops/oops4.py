# class a:
#     classvar2= "hey i'm a class var of class a"
#     def __init__(self):
#         self.var1 = "i'm var1"
#         self.classvar1 = "i'm an instance var of a"


# class b(a):
#     classvar2= "hey i'm a class var of class b"
#     def __init__(self):
#         self.var1 = "i'm var1"
#         # self.classvar1 = "i'm an instance var of b"
#         super().__init__()



# class_a = a()
# class_b= b()

# print(class_b.classvar1)
# print(class_b.var1)


# class employee:
#     def __init__(self, aname, asalary):
#         self.name = aname
#         self.salary = asalary


#     def __add__(self, other):
#         return self.salary + other.salary
    
#     def __str__(self):
#         return f"This is the object {self.name} and his salary is {self.salary}"
    
#     def __truediv__(self, other):
#         return self.salary / other.salary

# ashish = employee("ashish", 555)
# karan = employee("karan", 666)

# # print(ashish.salary+ karan.salary)
# print(ashish+karan)
# print(ashish)
# print(karan)
# print(ashish/karan)


# from abc import ABC, abstractclassmethod
# class animal(ABC):
#     @abstractclassmethod
#     def sound(self):
#         pass
#     def sleep(self):
#         pass


# class dog(animal):
#     def sound(self):
#         print("bhaw bhaw")


# class cat(animal):
#     def sound(self):
#         print("meow meow")



# tommy = dog()
# kitty = cat()

# tommy.sound()
# kitty.sound()
# print(tommy)

