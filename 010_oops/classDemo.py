

class Pen:
    price=10
    company='Cello'
    color = 'red'

    def to_write(self):
        print('write method calling')
        print(self.price, self.color,self.company)

p = Pen()
p.price=100
p.to_write()

p1 = Pen()
p1.to_write()

p2 = Pen()
p2.to_write()