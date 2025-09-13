# st = {
#     "name":"Tisha",
#     "email":"tisha@gmail.com",
#     "lang":["Guj","Hinidn","eng"]
# }

# print(st)
# print(st['name'])
# print(st.get('name'))


# st['name'] = "Zeel"
# st.update({"subject":"Python","stram":"IT"})
# print(st['lang'][0])

s = dict(name="devanshi",email="devanshi@gmail.com")

# print(s)
# print(s['name'])
# print(s.get('name'))
# print(s.keys())
# print(s.values())
# print(s.items())


# for i,j in s.items():
#     print(i,j)

# s['name1']="sunil"
# s.update({"name":"sunil","phone":"787878787"})
# s.pop('name')
# s.popitem()
# s.clear()
# print(s)

# students = {
#     "Zeel":{
#         "email":"zeel@gmail.com",
#         "phone":"748568574"
#     },
#     "Jenil":{
#         "email":"jenil@gmail.com",
#         "Phone":"7485968574"
#     }
# }

# for i,j in students.items():
#     print(i)
#     for a,b in j.items():
#         print(a,b)


# x = ('key1', 'key2', 'key3')
# y = "Hello"

# thisdict = dict.fromkeys(x,y)

# print(thisdict)

l = [1,2,3,4,5]


k = dict.fromkeys(l,a)
print(k)