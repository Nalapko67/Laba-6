import math

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        common = math.gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def input_fraction(self):
        self.numerator = int(input("Enter numerator: "))
        den = int(input("Enter denominator: "))
        while den == 0:
            print("Denominator cannot be zero. Try again.")
            den = int(input("Enter denominator: "))
        self.denominator = den
        self._simplify()

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    def calculate_value(self):
        val = self.numerator / self.denominator
        print(f"Decimal value: {val}")
        return val

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

def main():
    f1 = Fraction()
    f2 = Fraction()

    print("Enter first fraction:")
    f1.input_fraction()

    print("Enter second fraction:")
    f2.input_fraction()

    print("\nFirst fraction:")
    f1.display()
    f1.calculate_value()

    print("\nSecond fraction:")
    f2.display()
    f2.calculate_value()

    print("\nAddition:")
    result_add = f1 + f2
    result_add.display()

    print("\nSubtraction:")
    result_sub = f1 - f2
    result_sub.display()

    print("\nMultiplication:")
    result_mul = f1 * f2
    result_mul.display()

    print("\nDivision:")
    result_div = f1 / f2
    result_div.display()

if __name__ == "__main__":
    main()