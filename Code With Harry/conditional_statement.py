user_age = int(input("Enter your age: "))

if (user_age<=0):
    print("Enter correct age")
elif(user_age<18):
    print("Not eligible")
elif(user_age==18):
    print("You can come for drive test")
else:
    print("you're already eligible for the license")


list = [1,2,3]
print(5 in list)
if 5 in list:
    print("5 in list")
else:
    print("not in list")

print(3 in list)
if 3 in list:
    print("3 in list")
else:
    print("not in list")