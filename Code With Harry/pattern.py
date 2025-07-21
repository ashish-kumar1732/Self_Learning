# # Exercise - Pattern Printing

# bool= input("Choose value True or False:")
# str_no = int(input("enter te row no:"))

# if bool=="True":
#    i = 1
#    while(i<=str_no):
#       print(i*"*", end="\n")
#       i +=1

# elif bool=="False":
#    i=str_no
#    while(i>0):
#       print(i*"*", end="\n")
#       i -=1
# else:
#    print("You have entered wrong bool value")

bool_input = input("Choose value True or False:").strip()
str_no = int(input("Enter the row number:"))

# Convert the string input to a boolean
if bool_input.lower() == "true":
    i = 1
    while i <= str_no:
        print("*" * i)
        i += 1

elif bool_input.lower() == "false":
    i = str_no
    while i > 0:
        print("*" * i)
        i -= 1

else:
    print("You have entered a wrong bool value")