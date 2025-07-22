# l=15
# def function1():
#     global l
#     l=l+15
#     print(l)

# function1()


# def ashish():
#     x=30
#     def ram():
#         global x ### yeh ek step back nhi jayega, instead of global mei x ko find karega, 
#                  ### if find then will change it's value otherwise x ko globally initialize kar dega
#         x=90
#     print("before calling ram x:",x)
#     ram()
#     print("after calling ram x:",x)

# ashish()
# print(x) ### that's why it will print 90


### Quiz

x=89
def ashish():
    x=30
    def ram():
        global x
        x=90
    ram()
    print("after calling ram x:",x)

ashish()
print(x)