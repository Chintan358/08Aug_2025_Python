
class Sample:
    id = 10
    name="abc"

    def display(self):
        return f"my name is {self.name} and id is {self.id} "
    
class Demo:
    s = Sample()
    def show(self):
        return "sho calling"
    
d = Demo()
d.s.display()
print(d.s.display())
