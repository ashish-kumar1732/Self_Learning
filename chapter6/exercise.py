########### print a table ###################

# num= int(input("Enter a num: "))

# for i in range(1,11):
#     print(f"{num} X {i}: {num*i}")


######### add the name in a list which start with "J"

# name=["ashish","harry","Jerry","ross","joey","jack"]

# for i in range(len(name)):
#        check_name = (name[i].lower)
#        if(check_name().startswith("j")):
#               print(f"Hey! {name[i]}")
#     #    else:
#     #        pass



########## for prime number ############

# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Number is not prime")
# else:
#     for i in range(2, num): # for 2 --- range(2, 2) is an empty range — it produces no values. 
#                             # So the loop body is skipped entirely.

#         if num % i == 0:
#             print("Number is not prime")
#             break
#     else:
#         print("Number is prime")
          

########## sum using while loop ###########

# num= int(input("Enter a num: "))
# i=1
# sum=0
# while(i<=num):
#     sum +=i
#     i +=1
# print(sum)


########### Factorial ##############

# num = int(input("Enter your number: "))
# factorial=1
# for i in range(1, num+1):
#     factorial= factorial*i


# print(factorial)


############ Star Pattern ############

# num = int(input("enter a num "))

# for i in range(1, num+1):
#       print(" "*(num-i), end="")
#       print("*"*(2*i-1), end="")
#       print("\n")


# num = int(input("Enter a number: "))

# for i in range(1, num+1):
#         print("*"*i)


# num = int(input("Enter a number: "))

# for i in range(1,num+1):
#     if(i==1 or i==num):
#             print("*"*num, end="")
#     else:
#             print("*", end="")
#             print(" "*(num-2), end="")
#             print("*", end="")
#     print("")


######### Multiplication Table In reverse Order #########


# num = int(input("Enter a num: "))

# for i in range(1,11):
#     print(f"{num} X {11-i}: {num*(11-i)}")


## Greatest Number ##

# def Greatest_Num(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is the greatest num")
#     elif(b>c and b>a):
#         print(f"{b} is the greatest num")
#     elif(c>a and c>b):
#         print(f"{c} is the greatest num")
#     else:
#         print("you have entered two same numbers")

# num1= int(input("Enter a num: "))
# num2= int(input("Enter a num: ")) 
# num3= int(input("Enter a num: "))

# Greatest_Num(num1,num2,num3)

