"""
fg gfgf gfgdf
"""
class A :
    """
        Docstring for A
    """
    def abc(self):
        """
        Docstring for abc
        
        :param self: Description
        """
        print("abc calling")

a = A()
print(a.__doc__)
print(a.abc.__doc__)