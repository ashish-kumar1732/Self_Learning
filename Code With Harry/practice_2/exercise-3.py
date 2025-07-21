# #### Guessing number quiz

# no= 15
# print("You have 9 guess")
# guess=9
# num = int(input("guess a number bw 1 to 25: "))
# attempt=1

# while(guess!=1):

#     if num <=0 or num> 25:
#         print("out of range, enter again")
#         guess=guess-1
#         print(f"guess left {guess}")
#         num = int(input("guess a number again bw 1 to 25: "))
        

#     else:
#         if num == no:
#            print(f"you guess the number {no} in guess no. {attempt}")
#            break
#         else:
#            guess=guess-1
#            print(f"guess left {guess}")

#            if num>no:
#                 num = int(input("guessed number is bigger please decrease: "))          

#            elif guess ==1:
#                 if num == no:
#                  print(f"you guess the number {no} in guess no. {attempt}")
#                  break

#                 else:
#                  print("sorry you're out of guess numbers, but nice tried")
#                  break
#            else:
#                 num = int(input("guessed number is lesser please increase: "))
                 
        
#     attempt=attempt+1

import random
no = random.randint(1,26)
guess = 9
attempt = 1

print("You have 9 guesses")

while guess > 0:
    num = int(input("Guess a number between 1 to 25: "))

    if num <= 0 or num > 25:
        print("Out of range, please enter a number between 1 and 25.")
        guess -= 1
        print(f"Guesses left: {guess}")
    elif num == no:
        print(f"🎉 You guessed the number {no} on attempt {attempt}!")
        break
    else:
        guess -= 1
        print(f"Guesses left: {guess}")
        if num > no:
            print("Too high! Try a smaller number.")
        else:
            print("Too low! Try a larger number.")
    
    if guess == 0:
        print("😢 Sorry, you're out of guesses. Better luck next time!")
    
    attempt += 1