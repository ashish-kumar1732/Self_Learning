f = open("ash2.txt", "rt")
print(f.readline())
f.close()

with open ("ash2.txt") as f:
    a = f.readline()
    print(a)