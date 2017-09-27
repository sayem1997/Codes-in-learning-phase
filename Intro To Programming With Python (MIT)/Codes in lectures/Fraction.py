class Fraction(object):

    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int, "Integer is not used!"
        self.num = num
        self.denom =  denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        return Fraction((self.num * other.denom + other.num * self.denom), (self.denom * other.denom))

    def __sub__(self, other):
        return Fraction((self.num * other.denom - other.num * self.denom), (self.denom * other.denom))

    def __float__(self, other):
        return (self.num * other.denom + other.num * self.denom) / (self.denom * other.denom)


frac_1 = Fraction(3,4)
frac_2 = Fraction(5,6)

print(frac_1 + frac_2)