import random
import math
# This is a file of the little test snippets of code while reading the book. They're not exercises, rather test of the code provided and some other idaes that arose. 
class myClass:
    # Initializes the class
    def __init__(self, iterable):
        self.iterable = iterable
    # Returns the sum of all the values of an iterable 
    def mySum(self):
        total = 0
        for val in self.iterable:
            total += val
        return total
    # Returns the max value out of an iterable
    def myMax(self):
        max_value = self.iterable[0]
        for val in self.iterable:
            if val > max_value:
                max_value = val
        return max_value
    # Returns a random value out of an iterable
    def myRandom(self):
        random_index = random.randrange(0, len(self.iterable))
        return self.iterable[random_index]
    # Returns the index of the max value out of an iterable
    def myMaxIndex(self):
        index = 0
        for j in range(len(self.iterable)):
            if self.iterable[j] > self.iterable[index]:
                index = j
        return index
    # Search for a value inside an iterable. Returns True if found, False if not. 
    def search(self, target):
        for value in self.iterable:
            if value == target:
                return True
        return False
    # Multiplies each value out of an iterable by the factor provided. Returns the iterable with the multiplied values. 
    def scale(self, factor):
        number_list = []
        for i in range(len(self.iterable)):
            number_list.append(self.iterable[i] * factor)
        return number_list
    # Turns a list of values into list of absolutes, then returns the maximum |x|
    def absMag(self):
        return max(self.iterable, key=lambda x: x if x >= 0 else -x)
    # Returns the square root of the sum of a list
    def sumroot(self):
        added_list = self.mySum()
        return math.sqrt(added_list)
    # Returns the integer square root of the sum of a list
    def sumiroot(self):
        added_list = self.mySum()
        return math.isqrt(added_list)
    def isumdivision(self, divisor):
        added_list = self.mySum()
        quotient, remainder = divmod(added_list, divisor)
        print(f'Quotient: {quotient}')
        print(f'Remainder: {remainder}')
test_list = [1, 9, 3, 4, 5, 6, 7, 8, -10]
myList = myClass(test_list)
print(myList.myMax())
print(myList.myMaxIndex())
print(myList.search(3))
print(myList.search(10))
print(myList.scale(4))
print(myList.absMag())
print(myList.sumroot())
print(myList.sumiroot())
myList.isumdivision(4)

class generators:
    # Class initialization
    def __init__(self, iterations):
        self.iterations = iterations
    # A very elegant fibbonaci generator it returns the first {iterations} amount of numbers in the fibbonaci sequence
    def fibbonaci(self):
        a, b = 0, 1
        i = 0
        while i < self.iterations:
            yield a
            a, b = b, a+b
            i += 1
my_generators = generators(10)
print([value for value in my_generators.fibbonaci()])