
def is_prime(num):
    if num<=1:
        print(f"{num} is not a prime number")
    else:
        for i in range(2, num):
            if num%i==0:
                return False
        return True
            

for i in range(0,101):
    if is_prime(i):
                 print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
