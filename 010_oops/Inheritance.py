
# class Pen:
#     price = 10
#     color = "RED"
#     company="CEllo"

#     def display(self):
#         print(self.price,self.color,self.company)

# class Notebook(Pen):
#     pages = 100

#     def show(self):
#         self.price=50
#         print(self.price,self.color,self.company,self.pages)

# class Bag(Notebook):  -multilevel
# class Bag(Pen) : Hierarchical 
# class Bag(Pen,Notebook)  :multiple

# p = Pen()
# p.display()
# n = Notebook()
# n.show()


# class Clg:

#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email

#     def display(self):
#         print(self.id,self.name,self.email)

# class Student(Clg):

#     def __init__(self, id, name, email):
#         super().__init__(id, name, email)
       

#     def show(self):
#         print(self.id,self.name,self.email)

# # c = Clg(10,"Jenil","jenil@gmail.com")
# # c.display()

# s = Student(10,"Tisha","tisha@gmail.com")
# s.show()
# s.display()


# class Animal : 

#     def __init__(self,name):
#         self.name=name

#     def sleep(self):
#         print("Animal is sleeping")

#     def eat(self):
#         print("animla is eating")

# class Dog(Animal):

#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed=breed

#     def bark(self):
#         print(f"the dog {self.name} of breeed {self.breed} is barking")


# d  = Dog("Tommy","german shepherd")
# d.bark()
# d.sleep()
# d.eat()


class A:
    def __init__(self):
        print("A constucor calling")

class B(A):
    def __init__(self):
        super().__init__()
        print("B const calling")

b =  B()
