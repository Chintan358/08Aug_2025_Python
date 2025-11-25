import copy

l = [[1,2,3],[4,5,6]]

k = copy.copy(l)
# k[0][0] = 10
# print(k)
# print(l)
# k[0] = [10,20,30]
# print(k)
# print(l)


a = copy.deepcopy(l)
# a[0][0] = 50
# print(a)
# print(l)
a[0] = [10,20,30]
print(a)
print(l)