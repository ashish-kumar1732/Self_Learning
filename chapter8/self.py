class employee:
    language="JavaScript"
    book="Alchemist"
    def getinfo(self):
        print(f"The language is {self.language} and the book is {self.book}")
    @staticmethod ## by this static method we can call it by without passing parameters
    def greet():
        print("Good Afternoon!")
ashish=employee()

ashish.language= "Python"

# employee.getinfo(ashish)
ashish.getinfo()
ashish.greet()