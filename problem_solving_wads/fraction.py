from problem_solving_wads.gcd import gcd


class Fraction:
    def __init__(self, top: int, bottom: int = 1):
        assert all(
            isinstance(x, int) for x in (top, bottom)
        ), "Non integer values passed as arguments"

        if bottom < 0:
            top = abs(top) * -1
            bottom = abs(bottom)
        common = gcd(abs(top), abs(bottom))
        self.num = top // common
        self.den = bottom // common

    def __str__(self):
        if not (self.num % self.den):
            return f"{self.num//self.den}"
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self}>"

    def __add__(self, other):
        new_num = (self.num * other.den) + (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = (self.num * other.den) - (self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other):
        return (self.num / self.den) > (other.num / other.den)

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return (self.num / self.den) < (other.num / other.den)

    def __le__(self, other):
        return self < other or self == other

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den
