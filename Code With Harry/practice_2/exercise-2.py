## Faulty Calculator ##
operand1 = int(input("enter first num: "))
oper= input("enter operator like +,-,*,// : ")
operand2 = int(input("enter second num: "))

if oper =="+":
    if operand1== 5 and operand2==7:
        print(int("30"))
    else:
        print(operand1+operand2)
elif oper =="-":
    if operand1== 10 and operand2==3:
        print(int("15"))
    else:
        print(operand1-operand2)
elif oper =="*":
    if operand1== 9 and operand2==2:
        print(int("36"))
    else:
        print(operand1*operand2)
elif oper =="//":
    if operand1== 14 and operand2==2:
        print(int("10"))
    else:
        print(operand1//operand2)
else:
    print("you have given either wrong input or operatpr!")