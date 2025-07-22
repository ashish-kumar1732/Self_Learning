import random

list1=["Snack","Water","Gun"]
computer_choice= random.choice(list1)

player_choice= input("Enter your choice: ").strip().capitalize()

if player_choice in list1:
    if player_choice.lower()=="snack" and computer_choice.lower()=="water":
        print(f"computer's choice was {computer_choice}")
        print("Player is winner 🥳")
    # elif player_choice=="snack" and computer_choice=="gun":
    #     print("computer is winner 🥳")
    elif player_choice.lower()=="water" and computer_choice.lower()=="gun":
        print(f"computer's choice was {computer_choice}")
        print("Player is winner 🥳")
    # elif player_choice=="water" and computer_choice=="snack":
    #     print("computer is winner 🥳")
    elif player_choice.lower()=="gun" and computer_choice.lower()=="snack":
        print(f"computer's choice was {computer_choice}")
        print("Player is winner 🥳")
    else:
        print(f"computer's choice was {computer_choice}")
        print("Computer is winner 🥳")
    
else:
    print("You have entered wrong identity, Please try again")