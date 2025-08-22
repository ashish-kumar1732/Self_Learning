# def function_name(a,b):
#       print(a,b)


# function_name("ashosh","ash")


# def funargs(*args):
#     # print(args[1])
#     for item in args:
#         print(item) # Always print as a tuple

# names = ["ashish","ping pong"]

# funargs(*names)


# def funargs(nor,*args):
#     # print(args[1])
#     print(nor)
#     for item in args:
#         print(item) # Always print as a tuple

# names = ["ashish","ping pong"]
# nor = "hello i am normal and these are the students: "
# funargs(nor, *names)


def funkwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

names = {"ashhosh": "cr", "as": "fitness"}
funkwargs(**names)
