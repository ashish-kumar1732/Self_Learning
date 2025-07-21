# ####### Health Management System ######

# def getdata():
#     import datetime
#     return datetime.datetime.now()

# user_name = input("enter name of user: ").strip()

# if user_name.lower()=="krishna":
#     type_plan=input("what you want to enter exercise or diet: ").strip()
#     if type_plan.lower()=="diet":
#         with open("krishna_diet.txt", "w") as f:
#             content=input("add diet:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#     elif type_plan.lower()=="exercise":
#         with open("krishna_exercise.txt", "w") as f:
#             content=input("add exercise:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#     else:
#         print("You have entered wrong type of plan")
    
# elif user_name.lower()=="ram":
#     type_plan=input("what you want to enter exercise or diet: ").strip()
#     if type_plan.lower()=="diet":
#         with open("ram_diet.txt", "w") as f:
#             content=input("add diet:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#     elif type_plan.lower()=="exercise":
#         with open("ram_exercise.txt", "w") as f:
#             content=input("add exercise:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#     else:
#         print("You have entered wrong type of plan")

# elif user_name.lower()=="shyam":
#     type_plan=input("what you want to enter exercise or diet: ").strip()
#     if type_plan.lower()=="diet":
#         with open("shyam_diet.txt", "w") as f:
#             content=input("add diet:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#             print("\n")
#     elif type_plan.lower()=="exercise":
#         with open("shyam_exercise.txt", "w") as f:
#             content=input("add exercise:")
#             a=getdata()
#             f.write([a])
#             f.write(content)
#             print("\n")
#     else:
#         print("You have entered wrong type of plan")

# else:
#     print("You entered unregistered user name")

import datetime

def getdata():
    return datetime.datetime.now().strftime("[%d/%m/%Y, %H:%M:%S]")

def save_plan(user, plan_type, content):
    filename = f"{user.lower()}_{plan_type.lower()}.txt"
    with open(filename, "a") as f:
        timestamp = getdata()
        f.write(f"{timestamp} {content}\n")

user_name = input("Enter name of user: ").strip().lower()

if user_name in ["krishna", "ram", "shyam"]:
    type_plan = input("What do you want to enter — exercise or diet: ").strip().lower()
    if type_plan in ["exercise", "diet"]:
        content = input(f"Add {type_plan}: ").strip()
        save_plan(user_name, type_plan, content)
        print(f"{type_plan.capitalize()} saved successfully for {user_name.capitalize()} 🗂️")
    else:
        print("⚠️ You have entered wrong type of plan")
else:
    print("❌ You entered an unregistered user name")