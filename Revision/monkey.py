import Sample


def test(self):
    print("test calling")


Sample.A.show=test
obj = Sample.A()
obj.show()