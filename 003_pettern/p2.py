# *
# **
# ***
# ****
# *****

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()


# for i in range(5):
#         print("*"*(i+1))


# *****
# ****
# ***
# **
# *


# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     print("*"*i,end="")
#     print()






#      *
#     **
#    ***
#   ****
#  *****


# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()



# for i in range(5):
#     print(" "*(5-i),"*"*(i+1),end="")
#     print()


# *****
#  ****
#   ***
#    **
#     *

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# for i in range(5):
#     print(" "*(5-i),"* "*(i+1),end="")
#     print()


# * * * * *
#  * * * * 
#   * * *
#    * *
#     *



#      *
#     ***
#    *****
#   *******
#  *********


# for i in range(5):
#     for k in range(5-i):
#         print(" ",end="")
#     for j in range((i*2)+1):
#         print("*",end="")
#     print()
 
# 0 1  1
# 2 1  3
# 4 1  5
# 6 1  7
# 4 5  9



#      *
#     * *
#    *   *
#     * *
#      *


# lines = 7
# for i in range(lines):
#     print(" "*(lines-i),"* "*(i+1),end="")
#     print()
# for i in range(lines-1,0,-1):
#     print(" "*((lines-1)-i+2),"* "*(i),end="")
#     print()


# lines=5
# for i in range(lines):
#     for k in range(lines-i):
#         print(" ",end="")
#     for j in range(i+1):
#         if j==0 or j==(i):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# for i in range(lines-1,0,-1):
#     for k in range((lines-1)-i+2):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()





# 1
# 12
# 123
# 1234
# 12345


for i in range(5):
    for j in range(i+1):
        print(j+1,end="")
    print()

# 1
# 23
# 456
# 78910
# 1112131415

# 5
# 45
# 345
# 2345
# 12345

# 0
# 10
# 010
# 1010
# 01010