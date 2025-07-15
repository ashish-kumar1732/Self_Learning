def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
    
num= int(input("Enter a num: "))
print(f"Sum of n will be: {sum(num)}")