# lis = ["10","2", "5"]
# for i in range(len(lis)):
#     lis[i] = int(lis[i])

# lis[2] = lis[2] + 5

# print(lis[2])



#--------------------- Map ------------------



# lis = list(map(int, lis))

# lis[0] = lis[0] + 5

# print(lis[0])



# def sq(x):
#     return x*x

# lis = [1,5,4,8,6]


# lis = list(map(sq, lis))

# print(lis)



# lis = [1,5,4,8,6]

# lis = list(map(lambda x: x*x, lis))
# print(lis)


# def sq(a):
#     return a*a

# def cu(a):
#     return a*a*a

# lis= [sq, cu]


# for i in range(11):

#     lis2= list(map(lambda x:x(i), lis))
#     print(lis2)



#--------------------- Filter ------------------



# list1 = [1,2,3,4,5,6,7,8,9]

# def greater_num_5(num):
#     return num>5
         
# list2 = list(map(greater_num_5, list1))
# print(list2)




#--------------------- Reduce ------------------

lis = [1,2,3,4,5,6,7]
# num =0
# for i in lis:
#     num+=i

# print(num)

from functools import reduce

num = reduce(lambda x,y: x*y, lis)

print(num)