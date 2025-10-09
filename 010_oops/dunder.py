# class Demo:
#     id = 10
#     name="abc"
#     def __str__(self):
#         return f"my name is {self.name} and id is {self.id} "



# d = Demo()
# print(d)


class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b
       

c  =Calc(10,20)
c1 = Calc(30,40)

k = c+c1
print(k)