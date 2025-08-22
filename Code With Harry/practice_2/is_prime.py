# number =[44,5,99,74,47]

# for i in number:
#     num=number[i]
#     for j in range(2, num):
#       if i%j == 0:
#         print(f"{i} is Not a prime number")
# else:
#     print(f"{i} is a prime number")

number = [44,5,99,74,47]
for i in number:
    for j in range(2, i):
      if i%j !=0:
         print(f"{i} is a prime number")
         break
    
    else:
         continue


# number = [44, 5, 99, 74, 47]

# for i in number:
#     for j in range(2, i):
#         if i % j == 0:
#             print(f"{i} is Not a prime number")
#             break
#     else:
#         print(f"{i} is a prime number")


