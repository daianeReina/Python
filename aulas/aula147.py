# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str ******* returns the string representation of the object ******
# __repr__(self) - str ***** function returns the object representation in string format******

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return f'{self.x}, {self.y} '

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name} (x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Ponto(new_x, new_y)

    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other


p1 = Ponto(1, 2)
p2 = Ponto(3, 4)

# print(p1)
# print(repr(p2))  # object representation
# print(f'{p2!r}')  # object representation

p3 = p1 + p2  # factory method
print(p3)
print('P1 é maior que P2', p1 > p2)
