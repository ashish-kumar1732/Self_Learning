num = int(input("Choose a num: between 1 to 100: "))
import random
generated_num = random.randint(1,101)
print(f"Computer number was {generated_num}")

if(num==generated_num):
 print("Drew! play again")

elif(num>generated_num):
 print("Guest is winner")
else:
 print("Computer is winner")