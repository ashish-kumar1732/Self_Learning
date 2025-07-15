# def isprime(num):
#     isprime=True
#     if num<=1:
#         isprime=False
#     for i in range(2,(int((num+1)/2))):
#         if num%i==0:
#             isprime=False
#             break
#     return isprime

# def main():
#     num=10000000
#     for i in range(2,num+1):
#         if isprime(i):
#             print(i,end=' ')

# main()


# def is_prime(num):
#     if num <= 1:
#         print(f"{num} is not prime")
#         return

#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print(f"{num} is not prime")
#             return
#     print(f"{num} is a prime number")

# is_prime(4)


# def is_prime(num):
#     if num <= 1:
#         return False  # 0 and 1 are not prime
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Check numbers from 1 to 100
# for i in range(1, 101):
#     if is_prime(i):
#         print(f"{i} is a prime number")
#     else:
#         print(f"{i} is not a prime number")





# def is_prime(num):
#     if num<=1:
#         print(f"{num} is not a prime number")
#     else:
#             for i in range(2, num):
#                 if num%i==0:
#                     return False
#     return True
                

# for i in range(0,101):
#     if is_prime(i):
#                  print(f"{i} is a prime number")
#     else:
#         print(f"{i} is not a prime number")




def isprime(num):
    if num<=1:
        return False

    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
    

for i in range (0,101):
    if isprime(i):
        print(f"{i} is a prime number")

    else:
        print(f"{i} is not a prime number")