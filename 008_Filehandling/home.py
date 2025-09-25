# f = open("test.txt",'w')
# f.write("Hello python")
# f.close()

# f = open("test.txt",'a')
# f.write("\n Hello Java")
# f.close()

# f = open("test.txt",'r')
# # data = f.read()
# print(data)


# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     print(len(data))
#     # if 'Java' in data:
#     #     print(data)
#     if not data:
#         break


# f = open("test.txt",'r')
# data = f.readlines()
# print(data)


# with open('test.txt','r') as f:
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)


# with open('test1.txt','r+') as f:
#     f.write("something")
#     f.seek(0)
#     data = f.read()
#     print(data)


# with open('test1.txt','w+') as f:
#     f.write("something")
#     f.seek(0)
#     data = f.read()
#     print(data)

with open("logo-tops.png",'rb') as f:
    data = f.read()
    print(data)