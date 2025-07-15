class Number():
    def __init__(self,n):
        self.n=n

    def __add__(self,m):
        return self.n + m.n

n=Number(1)
m=Number(2)

print(n+m)