# class employee:
#     language="JavaScript"
#     book="Alchemist"
#     def getinfo(self):
#         print(f"The language is {self.language} and the book is {self.book}")
#     def __init__(self): ## dunder method which is automatically called
#         print("hey this is me, Groot!")
# ashish=employee()

# ashish.language= "Python"

# # employee.getinfo(ashish)
# ashish.getinfo()


class employee():
    language="Python"
    salary="120000"
    def __init__(self, language,salary):
        self.salary=salary
        self.language=language
        print("i am creating an object")

ashish=employee("JavaScript",130000)
print(ashish.language, ashish.salary)