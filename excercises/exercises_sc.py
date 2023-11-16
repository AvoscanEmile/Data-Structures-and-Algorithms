import sys
sys.path.insert(0, r'C:\\Users\\avosc\\Documents\\Emile\\Coding\\Python\\notes') # You must specify your own local path for the location of .\notes. 
from datastructures_sc import ValidationUtils
from icecream import ic
from abc import ABCMeta, abstractmethod
import math
from sympy import symbols, diff, simplify
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import re
from threading import Thread, Lock
import time
import random
from abc import ABC, abstractmethod
# 2.1 Software for fire detection, software for medical equipment, software for airplanes. 
# 2.2 An e-commerce website or a social media. Any piece of software's adaptibility is the difference between sales and bankruptcy. Adaptability is the difference between adapatation to a new market taking a couple months or a couple days. 
# 2.3 Class that takes selected text and returns it modified depending on the called method. This is a short example, not a throught implementation. 
class TextEditorModifier:
    def __init__(self, selected_text):
        self.selected_text = selected_text
        self.font_size = 12  # Default font size
        self.is_bold = False
        self.is_italic = False
        self.is_underline = False

    def font_size_up(self):
        self.font_size += 2

    def font_size_down(self):
        if self.font_size > 2:
            self.font_size -= 2

    def italic(self):
        self.is_italic = not self.is_italic

    def bold(self):
        self.is_bold = not self.is_bold

    def underline(self):
        self.is_underline = not self.is_underline
# 2.4 Flower class implementation
class Flower:
    def __init__(self, name = None, petals = None, price = None):
        self._name = ValidationUtils.validate_string(name, r'^[a-zA-Z_\s]+$', f'The provided name "{name}" of type {type(name)} must be a string consisting of only word characters.')
        self._petals = ValidationUtils.validate_positive_number(petals, f'The provided petals "{petals}" of type {type(petals)} must be a positive integer', types=int)
        self._price = ValidationUtils.validate_positive_number(price, f'The provided price "{price}" of type {type(price)} must be a positive float', types=float)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = ValidationUtils.validate_string(name, r'^[a-zA-Z_\s]+$', f'The provided name "{name}" of type {type(name)} must be a string consisting of only word characters.')
    @name.deleter
    def name(self):
        self._name = None
    @property
    def petals(self):
        return self._petals
    @petals.setter
    def petals(self, petals):
        self._petals = ValidationUtils.validate_positive_number(petals, f'The provided petals "{petals}" of type {type(petals)} must be a positive integer', types=int)
    @petals.deleter
    def petals(self):
        self._petals = None
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price):
        self._price = ValidationUtils.validate_positive_number(price, f'The provided price "{price}" of type {type(price)} must be a positive float', types=float)
    @price.deleter
    def price(self):
        self._price = None
# 2.5, 2.6, 2.7 All of these problems are solved on my implementation of the CreditClass class on .\notes\datastructures_sc.py
# 2.8 You can cause the third instance of the CreditClass class on the first loop by changing the range from range(1, 17) to range(1, 1668). Since 1667 * 3 = 5001
# 2.9, 2.10, 2.11, 2.12, 2.13, 2.14, 2.15 All of these problems are solved on my implementation of the Vector class on .\notes\datastructures_sc.py
# 2.16 max(0, start - stop + step - 1 // step) Works because its inclusive. If the range was not inclusive start - stop would be enough, by adding step - 1 you ensure that the range includes the stop inside the range itself and nothing else. max() ensures that the range steps are not negative. If the calculation returns a negative value, then the max automatically selects 0. 
# 2.17 The problem asks for a Diagram, but I took the liberty to actually make the classes. All classes inherit from object by default, it's not necessary to declare it explecitly. 
class Goat:
    def __init__(self, tail):
        self._tail = ValidationUtils.validate_positive_number(tail, f'Tails must either be a positive integer or float. {type(tail)} was provided.')
        self._isjumping = False
    @property
    def tail(self):
        return self._tail
    @tail.setter
    def tail(self, new_tail):
        self._tail = ValidationUtils.validate_positive_number(new_tail, f'Tails must either be a positive integer or float. {type(new_tail)} was provided.')
    @tail.deleter
    def tail(self):
        del self._tail
    def milk(self):
        return "I've got no milk, I'm a male goaat you baaHfoon." 
    def jump(self):
        self._isjumping ^= True
        return f'The goat is {"actually" if self._isjumping else "not"} jumping.'
class Pig:
    def __init__(self, nose):
        self._nose = ValidationUtils.validate_positive_number(nose, f'noses must either be a positive integer or float. {type(nose)} was provided.')
        self._eatenfood = []
        self._iswallowing = False
    @property
    def nose(self):
        return self._nose
    @nose.setter
    def nose(self, new_nose):
        self._nose = ValidationUtils.validate_positive_number(new_nose, f'noses must either be a positive integer or float. {type(new_nose)} was provided.')
    @nose.deleter
    def nose(self):
        del self._nose
    @property
    def eatenfood(self):
        return self._eatenfood
    @eatenfood.deleter
    def eatenfood(self):
        self._eatenfood = []
    def eat(self, food):
        self._eatenfood.append(ValidationUtils.validate_string(food, r'^[a-zA-Z_\s]+$', f'Food must be a string consisting of English Alphabet characters. "{food}" of type {type(food)} was provided'))
    def wallow(self):
        self._iswallowing ^= True
        return f'The pig is {"currently" if self._iswallowing else "not"} wallowing.'
class Horse: 
    def __init__(self, color, height):
        self._color = ValidationUtils.validate_string(color, r'^[a-zA-Z_\s]+$', f'Color must be a string consisting of English Alphabet characters. "{color}" of type {type(color)} was provided.')
        self._height = ValidationUtils.validate_positive_number(height, f'Height must be provided as a positive number (float or intenger) representing cm. "{height}" of type {type(height)} was provided.')
        self._isrunning = False
        self._isjumping = False
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, new_color):
        self._color = ValidationUtils.validate_string(new_color, r'^[a-zA-Z_\s]+$', f'Color must be a string consisting of English Alphabet characters. "{new_color}" of type {type(new_color)} was provided.')
    @color.deleter
    def color(self):
        del self._color
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, new_height):
        self._height = ValidationUtils.validate_positive_number(new_height, f'Height must be provided as a positive number (float or intenger) representing cm. "{new_height}" of type {type(new_height)} was provided.')
    @height.deleter
    def height(self):
        del self._height
    def run(self):
        self._isrunning ^= True
        return f'The horse is {"currently" if self._isrunning else "not"} running.'
    def jump(self):
        self._isjumping ^= True
        return f'The horse is {"currently" if self._isjumping else "not"} jumping.'    
class Racer(Horse):
    def __init__(self, color, height):
        super().__init__(color, height)
        self._isracing = False
    def race(self):
        self._isracing ^= True
        return f'The horse is {"currently" if self._isracing else "not"} racing.'          
class Equestrian(Horse):
    def __init__(self, color, height, weight, trained = True):
        super().__init__(color, height)
        self._weight = ValidationUtils.validate_positive_number(weight, f'Weight must be a positive number (int or float). "{weight}" of type {type(weight)} was provided.')
        self._istroting = False
        self._istrained = ValidationUtils.validate_boolean(trained, f'Trained must be a boolean value. "{trained}" of type {type(trained)} was provided')
    def trot(self):
        self._istroting ^= True
        return f'The horse is {"currently" if self._istroting else "not"} troting.'           
    @property 
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        self._weight = ValidationUtils.validate_positive_number(weight, f'Weight must be a positive number (int or float). "{weight}" of type {type(weight)} was provided.')
    @weight.deleter
    def weight(self):
        del self._weight
    @property
    def istrained(self):
        return self._istrained
    @istrained.setter
    def istrained(self, trained):
        self._istrained = ValidationUtils.validate_boolean(trained, f'Trained must be a boolean value. "{trained}" of type {type(trained)} was provided')
    @istrained.deleter
    def istrained(self):
        del self._istrained
    def is_trained(self):
        return f'The horse is {"well" if self.istrained else "not"} trained'
# Progression classes for some of the solutions. 
class Progression: 
    def __init__(self, start=0):
        self._current = ValidationUtils.validate_positive_number(start, f'Start must be an integer. "{start}" of type {type(start)} provided.', types=int)
    def _advance(self):
        self._current += 1
    def __next__(self):
        if self._current is None: 
            raise StopIteration()
        else: 
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self, n):
        print( ",".join(str(next(self)) for j in range(n)))
class ArithmeticProgresion(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = ValidationUtils.validate_positive_number(increment, f'Start must be an integer. "{increment}" of type {type(increment)} provided.', types=int)
    def _advance(self):
        self._current += self._increment
class FibbonaciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        validated_second = ValidationUtils.validate_positive_number(second, f'Start must be an integer. "{second}" of type {type(second)} provided.', types=int)
        self._prev = second - first
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
# 2.18 This function returns the n value out of a fibbonacci sequence that starts with two provided values, if used with (2, 2, 8) you get the answer to this problem. 
def fibValue(first, second, n):
    fib_progression = FibbonaciProgression(first, second)
    for _ in range(n):
        next(fib_progression)
    return fib_progression._current
# 2.19 A call to this function with the parameters 128 and 2^56 = 72057594037927940 will yield a exactly 2^63 since 2^63 / 2^7 = 2^56. The solution to the problem is 2^56.
def ArithValue(increment, n):
    arith_progression = ArithmeticProgresion(increment)
    for _ in range(n):
        next(arith_progression)
    return arith_progression._current
# 2.20 Deeper inheritance hierarchies can introduce a performance overhead due to the need to navigate through multiple layers to resolve method calls. This can impact runtime performance, especially if the hierarchy is extensive.
# 2.21 Shallow inheritance hierarchies don't present too much of a problem performance wise, but a dependance on a single parent class may make the code monolithic. In the sense that this single class does too much and makes maintenance and changes difficult to make. 
# 2.22, 2.23 Sequence implementation with added __eq__ and __lt__ methods
class mySequence(metaclass=ABCMeta):
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def __getitem__(self, j):
        pass
    def __contains__(self, value):
        for j in range(len(self)):
            if self[j] == value:
                return True
        return False
    def index(self, value):
        for j in range(len(self)):
            if self[j] == value:
                return j
        return ValueError("Value not in sequence")
    def counter(self, value):
        k = 0 
        for j in range(len(self)):
            if self[j] == value:
                k += 1
        return k
    def __eq__(self, other):
        if len(self) == len(other):
            return all([self[j] == other[j] for j in range(len(self))])
        else: 
            return False
    def __lt__(self, other):
        if len(self) == len(other):
            for j in range(len(self)):
                if self[j] < other[j]:
                    return True
                elif self[j] > other[j]:
                    return False
            return False
        else: 
            raise ValueError('The provided sequences are not of the same length')
# 2.24 Instead of actually drawing a class I decided to declare classes with simple code within them, merely as placeholders for the architecture of the hypothetical project. 
class Book: 
    def __init__(self, title, author, year, content):
        self._title = title
        self._author = author
        self._year = year
        self._content = content
        self._current_book = None
class Customer:
    def __init__(self, name, email, booklist):
        self._name = name
        self._email = email
        self._booklist = booklist
    def buy_book(self, book):
        self._booklist += book
    def view_booklist(self):
        return self._booklist
    def read_book(self, book):
        if book in self._booklist:
            self._current_book = book
class Library:
    def __init__(self, booklist):
        self._booklist = booklist
    def add_book(self, book):
        self._booklist += book
    def get_book(self, book):
        if book in self._booklist:
            return book
class EbookReader(Customer):
    def __init__(self, name, email, booklist, current_page):
        super().__init__(name, email, booklist)
        self._current_page = current_page
    def read_current_book(self):
        return self._current_book
    def prev_page(self):
        if self._current_page <= 1:
            return "You're already on the first page"
        else: 
            self._current_page -= 1
    def next_page(self):
        self._current_page += 1
# 2.25 I solved this one on my implementation of the Vector class on .\notes\datastructures_sc.py
# 2.26 Reverse sequence iterator implementation
class ReverseSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = 0
    def __next__(self):
        self._k -= 1
        if abs(self._k) <= len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
    def __iter__(self):
        return self
# 2.27 Efficient implementation of contains. The default range implementation in python verifies value by value, this version takes advantage of the mathematical properties of a range. 
class EfficientRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.num_steps = (stop - start) // step
    def __contains__(self, value):
        return (value - self.start) % self.step == 0 and 0 <= (value - self.start) // self.step <= self.num_steps
# 2.28, 2.29, 2.30 These solutions are provided in my implementation of the PredatoryCreditClass on .\notes\datastructures_sc.py
# 2.31 Absolute difference progression created by inheriting from Progresssion. 
class AbsProgression(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = ValidationUtils.validate_positive_number(second, f'Start must be an integer. "{second}" of type {type(second)} provided.', types=int)
    def _advance(self):
        self._prev, self._current = self._current, abs(self._current - self._prev)
# 2.32 Square Root Progression that inherits from Progression
class SqrProgression(Progression):
    def __init__(self, start=65536):
        super().__init__(start)
    def _advance(self):
        self._current = math.sqrt(self._current)
# 2.33 First Derivative from polynomial on standard notation using sympy. I decided for it to be a function instead of a program, but it can be turned into a program by simply adding some form of input handling. 
def find_derivative(poly_str):
    x = symbols('x')
    try:
        poly_expr = simplify(poly_str)
        derivative = diff(poly_expr, x)
        return derivative
    except Exception as e:
        return f"Error: {e}"
# 2.34 Python program that reads a file as a string, turns them into lowercase, cleans them from any character that is not a english alphabet one and finally displays a counter of every character as a bar-chart. To run it you must simple call call_program(). A possible future implementation could be used to run more file formats other than plain text. 
# Uses tkinter to open a file explorer to select the file that will be read. For the moment this only supports the filetypes inside filetypes=. It might also work with other plain text files. 
def open_text_file():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[
            ("Text files", "*.txt"),
            ("Markdown files", "*.md"),
            ("CSV files", "*.csv")
        ]
    )
    if file_path:
        with open(file_path, 'r') as file:
            text_content = file.read()
        return text_content
    else:
        print("No text file selected.")
        return None
# Cleans a string and creates a counter dictionary of the characters of that string. 
def count_lowercase_alphabets(input_string):
    # Use regex to remove non-alphabetic characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-z]', '', input_string.lower())
    # Count the occurrences of each lowercase English alphabet character
    counts = {}
    for char in cleaned_string:
        counts[char] = counts.get(char, 0) + 1
    return dict(sorted(counts.items()))
# Displays counter dictionary as a bar-chart. 
def plot_bar_chart(counts):
    letters = list(counts.keys())
    counts_values = list(counts.values())

    plt.bar(letters, counts_values)
    plt.xlabel('Lowercase Alphabets')
    plt.ylabel('Count')
    plt.title('Count of Lowercase Alphabets in the String')
    plt.show()
# Calls the whole program
def call_program():
    text_file_content = open_text_file()
    if text_file_content is not None:
        result = count_lowercase_alphabets(text_file_content)
        plot_bar_chart(result)
# 2.35 This three classes simulate the communication between alice and bob in pretty simple simulation of a Message Passing Interface (MPI). 
# Simple packet class at the base of the system. It will be called by the sender. 
class Packet:
    def __init__(self, content):
        self.content = content
# Sender class. It takes a Receiver instance and a form of storage (in this case a list) for the sent messages as arguments. It periodically sents packages to the list for being stored. 
class Sender:
    def __init__(self, receiver, sent_messages):
        self.receiver = receiver
        self.sent_messages = sent_messages

    def create_packet(self, content):
        packet = Packet(content)
        self.sent_messages.append(packet)
        self.receiver.receive_packet(packet)

    def periodically_create_packets(self, interval, content):
        while True:
            self.create_packet(content)
            time.sleep(interval)
# A receiver class, it takes the list of sent_messages as an argument. It periodically verifies if this list contains a package, and if it does it prints it and removes it from the list. 
class Receiver:
    def __init__(self, sent_messages):
        self.sent_messages = sent_messages
        self.lock = Lock()  # Lock to ensure thread-safe access to shared data

    def receive_packet(self, packet):
        with self.lock:
            print(f"Received packet: {packet.content}")
            self.sent_messages.remove(packet)

    def periodically_check_packets(self, interval):
        while True:
            with self.lock:
                if self.sent_messages:
                    print("Checking for packets...")
                    print("Unacknowledged packets:", [packet.content for packet in self.sent_messages])
                else:
                    print("No unacknowledged packets.")
            time.sleep(interval)

# Function to start the simulation of the interaction
def start_simulation():
    shared_messages = []  # Shared data structure to store sent messages

    bob_receiver = Receiver(shared_messages)
    alice_sender = Sender(bob_receiver, shared_messages)

    sender_thread = Thread(target=alice_sender.periodically_create_packets, args=(1, "Hello, Bob!"))
    receiver_thread = Thread(target=bob_receiver.periodically_check_packets, args=(2,))

    sender_thread.start()
    receiver_thread.start()

    sender_thread.join()
    receiver_thread.join()
# 2.36, 2.37 River simulation with Fishes and Bears that complies with the requisites of both problems. 

class Animal:
    def __init__(self, gender, strength):
        self.gender = gender
        self.strength = strength

    def __repr__(self):
        return f'{self.__class__.__name__[0]}'

class Bear(Animal):
    pass

class Fish(Animal):
    pass

def create_animal(gender, strength, animal_type):
    if animal_type == "Bear":
        return Bear(gender, strength)
    elif animal_type == "Fish":
        return Fish(gender, strength)
    else:
        raise ValueError("Invalid animal type")

def create_ecosystem(size, num_bears, num_fish):
    ecosystem = [None] * size

    for _ in range(num_bears):
        index = random.randint(0, size - 1)
        while ecosystem[index] is not None:
            index = random.randint(0, size - 1)
        gender = random.choice([True, False])  # True for male, False for female
        strength = random.uniform(1.0, 10.0)
        ecosystem[index] = create_animal(gender, strength, "Bear")

    for _ in range(num_fish):
        index = random.randint(0, size - 1)
        while ecosystem[index] is not None:
            index = random.randint(0, size - 1)
        gender = random.choice([True, False])  # True for male, False for female
        strength = random.uniform(1.0, 10.0)
        ecosystem[index] = create_animal(gender, strength, "Fish")

    return ecosystem

def display_ecosystem(ecosystem):
    print("".join(str(cell) if cell is not None else '.' for cell in ecosystem))

def survive_after_collision(animal1, animal2):
    if animal1.gender != animal2.gender:
        # Different genders, create a new instance
        return create_animal(random.choice([True, False]), max(animal1.strength, animal2.strength), animal1.__class__.__name__)

    # Same gender, the one with larger strength survives
    return animal1 if animal1.strength >= animal2.strength else animal2

def simulate_ecosystem(ecosystem, steps):
    size = len(ecosystem)

    for _ in range(steps):
        for i in range(size):
            if ecosystem[i] is not None:
                move_to = random.choice([i-1, i, i+1])
                if 0 <= move_to < size and ecosystem[move_to] is None:
                    ecosystem[move_to] = ecosystem[i]
                    ecosystem[i] = None
                elif 0 <= move_to < size and isinstance(ecosystem[move_to], type(ecosystem[i])):
                    # Collide, survive based on gender and strength
                    if random.choice([True, False]):
                        ecosystem[move_to] = survive_after_collision(ecosystem[move_to], ecosystem[i])
                        ecosystem[i] = None

        display_ecosystem(ecosystem)
        print()

def call_river():
    size_of_river = 10
    initial_bears = 5
    initial_fish = 5
    simulation_steps = 50

    ecosystem = create_ecosystem(size_of_river, initial_bears, initial_fish)
    display_ecosystem(ecosystem)
    print("\nSimulation:")
    simulate_ecosystem(ecosystem, simulation_steps)
# 2.38 Improved implementation of the code I did to solve 2.24. Library actually stores the books within it and the storage gets modified when customer takes from it. 
class NewBook:
    def __init__(self, title, author, year, content):
        self._title = title
        self._author = author
        self._year = year
        self._content = content

class NewLibrary:
    def __init__(self):
        self._booklist = {}

    def add_book(self, book, num_copies=1):
        if book._title in self._booklist:
            self._booklist[book._title] = (book, self._booklist[book._title][1] + num_copies)
        else:
            self._booklist[book._title] = (book, num_copies)

    def get_book(self, book_title, num_copies=1):
        if book_title in self._booklist and self._booklist[book_title][1] >= num_copies:
            book, quantity = self._booklist[book_title]
            self._booklist[book_title] = (book, quantity - num_copies)
            return book
        else:
            return None

class NewCustomer:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._booklist = {}

    def buy_book(self, library, book_title, num_copies=1):
        # Check if the book title is available in the library
        if library.get_book(book_title, num_copies) is not None:
            # Update the customer's booklist
            if book_title in self._booklist:
                self._booklist[book_title] += num_copies
            else:
                self._booklist[book_title] = num_copies

            print(f"You've successfully purchased {num_copies} copies of {book_title}.")
        else:
            print(f"Sorry, {book_title} is not available in sufficient quantity in the library.")

    def view_booklist(self):
        return self._booklist

    def read_book(self, book):
        if book in self._booklist:
            return book

class NewEbookReader(Customer):
    def __init__(self, name, email):
        super().__init__(name, email)
        self._current_page = 1

    def read_current_book(self):
        return {"book": self._current_book, "page": self._current_page}

    def prev_page(self):
        if self._current_page <= 1:
            return "You're already on the first page"
        else:
            self._current_page -= 1

    def next_page(self):
        self._current_page += 1
# This is a temporary test while the fully dedicated tests for these notes gets implemented. 
def test_library():
    # Assuming you already have the Book, Library, and EbookReader classes defined
    # Create an instance of Library and Customer
    library_instance = NewLibrary()
    # Add a list of 100 different books to the library
    for i in range(1, 101):
        book_title = f"Book{i}"
        author = f"Author{i}"
        year = 2000 + i
        content = f"Content of Book{i}"

        # Create an instance of Book
        book_instance = Book(title=book_title, author=author, year=year, content=content)

        # Add the book to the library
        library_instance.add_book(book_instance, num_copies=random.randint(1, 10))
    # Show the titles of all the books in _booklist
    ic(library_instance._booklist)
    # client_instance buys one of each book from the library, then print out the updated _booklist
    client_instance = NewCustomer('John', 'easd@dasf.com')
    for book in library_instance._booklist.keys():
        client_instance.buy_book(library_instance, book)
    ic(library_instance._booklist)
# 2.39 Inheritance hierarchy for the area and perimiter of multiple types of polygons. From the three types of triangles, to quadrilaterals, to regular polygons. 
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

class Quadrilateral(Polygon):
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3 + self.side4

class RegPolygon(Polygon):
    def __init__(self, side_length, side_amount):
        self.side_length = side_length
        self.side_amount = side_amount
    def area(self):
        cot_angle = 1 / math.tan(math.pi / self.side_amount)
        area = (1 / 4) * self.side_amount * self.side_length**2 * cot_angle
        return area
    def perimeter(self):
        return self.side_amount * self.side_length

class Pentagon(RegPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 5)

class Hexagon(RegPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 6)

class Octagon(RegPolygon):
    def __init__(self, side_length):
        super().__init__(side_length, 8)

class IsoscelesTriangle(Triangle):
    def __init__(self, base, equal_side):
        super().__init__(base, equal_side, equal_side)

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)

class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super().__init__(length, width, length, width)

class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side, side, side)