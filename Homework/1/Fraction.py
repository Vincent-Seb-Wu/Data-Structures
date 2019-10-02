class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:  
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        """
        create and return a new Fraction object, which is the sum of self + other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the sum of self + other.
        """
        
        return Fraction((self.numerator * other.denominator + self.denominator * other.numerator), (self.denominator * other.denominator))

    def __iadd__(self, other):
        """
        modify the self Fraction object, which adds other Fraction object value to self.

        :param other: Fraction -- the other fraction number.
        :return: self. The value of self should become the sum of self + other.
        """
        self.numerator += other.numerator

    def __sub__(self, other):
        """
        create and return a new Fraction object, which is the subtraction of self - other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the subtraction of self - other.
        """
        
        return Fraction((self.numerator * other.denominator - self.denominator * other.numerator), (self.denominator * other.denominator))

    def __mul__(self, other):
        """
        create and return a new Fraction object, which is the multiplication of self * other. 
        DO NOT MODIFY self.

        :param other: Fraction -- the other fraction number.
        :return: Fraction -- a **new** Fraction object, which is the multiplication of self * other.
        """
        
        return Fraction((self.numerator * other.numerator), (self.denominator * other.denominator))

    def __eq__(self, other):
        """
        Compare if self Fraction object has equal numerical value to the other Fraction object.
        Example: 2/3 == 4/6 --> True
                 2/3 == 2/3 --> True
        If you use the reduce() function here, it is fine.

        :param other: Fraction -- the other fraction number.

        :return: True if the float value of self is equal to other;
                 False if the float value of self is not equal to other.
        """
        if self.numerator / self.denominator == other.numerator / other.denominator:
            return True
        return False

    def reduce(self):
        """
        Reduces (Simpilifies) the self Fraction object. 
        Modifies both self.numerator and self.denominator.
        For example: 12 / 24 --> 1 / 2;  16 / 20 --> 4 / 5

        :return: Nothing.
        """
        
        if self.numerator > self.denominator:
            div = self.numerator
        else:
            div =  self.denominator
        
        for each in range(1, div):
            if self.numerator % each == 0 and self.denominator % each == 0:
                self.numerator = int(self.numerator / each)
                self.denominator = int(self.denominator / each)
        

    def __str__(self):
        """
        Displays the self Fraction object nicely. 
        Recommended format:
        Suppose,
        self.numerator = 5
        self.denominator = 6
        Then, should return "5 / 6"

        :return: The string representation of self Fraction object.
        """
        return str(self.numerator) + ' / ' + str(self.denominator)



'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    x = Fraction(3, 4)
    y = Fraction(4, 6)
    print(x)        # 3 / 4
    print(y)        # 4 / 6
    print(x + y)    # 34 / 24 or any value that is equal
    z = x + y
    print(x * y)    # 12 / 24 or any value that is equal
    print(x - y)    # 2 / 24 or any value that is equal
    y.reduce()
    print(y)        # 2 / 3
    z.reduce()
    print(z)        # 17 / 12

    print(z == Fraction(-17, -12))  # True
    print(z == Fraction(51, 36))  # True
    print(z == Fraction(-7, 4))   # False
    
if __name__ == '__main__':
    main()
