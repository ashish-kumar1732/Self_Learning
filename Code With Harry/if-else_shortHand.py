# a= int (input("Enter a: "))
# b=int (input("Enter b: "))
# print("a is big") if a>b else print("b is big")



##Function and Docstring

# def function1(a,b):
#     """This returns average of two values only"""
#     average= (a+b)//2
#     return average
# v= function1(5,15)
# print(function1.__doc__)
# print("average is:",v)


## Try Except
num1= input("enter a num:")
num2= input("enter a num:")

try:
    print("sum:", int(num1)+int(num2))

except Exception as e:
    print(e)

print("hello world")