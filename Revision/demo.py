
# def test():
#     print("print something...")

# def add(a,b):
#     print(f"addiion of {a} and {b} is {a+b}")

# def square(a):
#     return a*a


# def user(name="dgfgg",email="test@gmailc.om",phone=80000000):
#     print(name,email,phone)


# def count(*a):
#     print(a)

# count = lambda *a : print(a)

# test()
# add(100,20)
# user(phone=747474747)
# count(10,20,30,40,50)




l = [10,20,30,40,50,60,60]

# def dt(a):
#     return a/2

# kl = []
# for i in l:
#    k = dt(i)
#    kl.append(k)
# print(kl)

# kl = map(lambda a : a/2,l)
# print(list(kl))

l = ["Tisha","Devanshi","Zeel","Dhrivin","sunil"]

# k = map(lambda a : "Hello ,"+a ,l)
# print(list(k))

# def result(a):
#     if 'i' in a:
#         return a

# k = filter(lambda a :'i' in a,l)
# k = filter(lambda a :a.startswith('D'),l)
# print(list(k))

from functools import reduce

# a  =[10,20,5,68,9,8,45]

# def max(a,b):
#     print(a,b)
#     if a>b:
#         return a
#     else :
#         return b
    

a  =[10,20,5,68,9,8,45]
# x = a[0]
# for i in range(1,len(a)):
#     y = a[i]
#     k = max(x,y)
#     x = k
#     print(k)
# k = reduce(lambda i,j : i if i>j else j,a)
# print(k)

# l = [10,20,30,40,50]
# k = iter(l)
# print(next(k))
# print(next(k))

def square(a):
    for i in range(a):
       yield i*i
    

k = iter(square(10))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
