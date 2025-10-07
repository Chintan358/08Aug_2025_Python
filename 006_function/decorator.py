

# def beforeTest(test):
#     def wrapper():
#         print("call before test")
#         test()
#     return wrapper


# @beforeTest
# def test():
#     print("Test calling...")

# @beforeTest
# def demo():
#     print("Demo calling")


# test()
# demo()

# def add(calc):
#     def wrapper(*a):
#         print(a[0]+a[1])
#         calc(*a)
#     return wrapper

# def mul(calc):
#     def wrapper(*a):
#         print(a[0]*a[1])
#         calc(*a)
#     return wrapper

# @mul
# @add
# def calc(a,b):
#     print("Calc operation")


# calc(10,20)



# def decor(test):
#     def wrapper(*a):
#         print("before")
#         test(*a)
#         print("hello")
#     return wrapper


# @decor
# def test(a):
#     print("Testing")

# test(10)

# def only_number(func):
#     def wrapper(*a):
#         if not str(a[0]).isdigit():
#             print("Only numbers allowed")
#         else:
#          func(*a)
#     return wrapper


# @only_number
# def myfunc(a):
#     print(a)

# myfunc("10fdfd")