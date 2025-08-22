# def dunction():
#     print("subscribe it.")

# dunction2 = dunction
# del dunction
# dunction2()

# def func(num):
#     if num ==0:
#         return print
#     else:
#         return sum

# print(func(1))

# def func(jso):
#     jso("heya")

# func(print)

# def square(x):
#     return (x*x)

# print(square(5))

import time

def timer(func):
    def wrapper(*args):
        start= time.time()
        result= func(*args)
        end= time.time()
        total_time= end-start
        print(f"{func.__name__} ran in {round(total_time,2)} time")
        return result
    return wrapper

def calculate_time(x,y):
    time.sleep(x*y)

calculate= timer(calculate_time) 
calculate(2,5)
