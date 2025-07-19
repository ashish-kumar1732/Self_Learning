squared_num = {x:x**2 for x in range(1,11)}
print(squared_num)


### Another way to print this ###

for i in squared_num:
    print(f"Square of {i} is {i**2}")

print(squared_num.clear())