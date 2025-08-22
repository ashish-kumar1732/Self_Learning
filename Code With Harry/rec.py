##### Factorial by iteration

fact=1
def factorial(n):
    for i in range(1,n+1):
        global fact
        fact=i*fact
    
m= int(input("enter number:"))
factorial(m)
print(f"Factorial of {m}! is {fact}")
        

######## Factorial by recursion

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1) ### recursion use recursion stack to hold(calculation) data
    
#     """
#     5*factorial(4)
#     5*4*factorial(3)
#     5*4*3*factorial(2)
#     5*4*3*2*factorial(1) ## factorial 1 return 1, so loop over by getting factorial 1 value 1
#     5*4*3*2*1 ==120

#     """

# m= int(input("enter number:"))
# factorial(m)
# print(f"Factorial of {m}! by recursion is {factorial(m)}")

# def fibonacci(m):
#     if m==1:
#         return 0
#     elif m==2:
#         return 1
#     else:
#         return fibonacci(m-1)+fibonacci(m-2)
    
# m= int(input("enter number:"))
# fibonacci(m)
# print("fibonacci series is:", fibonacci(m))