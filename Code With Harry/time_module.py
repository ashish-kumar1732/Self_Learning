import time
intial = time.time()
k=0
while k<45:
    time.sleep(2)
    print("hello this is me, ash")
    k+=1 
print(f"time to run is {time.time()-intial}")

intial2 = time.time()

for i in range(46):
    print("hello this is me, ash")
print(f"time to run is {time.time()-intial2}")

# localtime = time.asctime(time.localtime(time.time()))
# print(localtime)