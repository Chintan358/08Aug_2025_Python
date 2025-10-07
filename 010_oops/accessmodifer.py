
class Demo:

    __name="xyz"
    email="xyz@gmail.com"

    def show(self):
        print(self.__name,self.email)

d = Demo()
print(dir(d))
d._Demo__name="abc"
d.show()