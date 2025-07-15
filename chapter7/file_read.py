# f = open("file.txt")
# data= f.read()
# print(data)
# f.close()


with open("file.txt") as f:
    print(f.read()) # without using f.close() function