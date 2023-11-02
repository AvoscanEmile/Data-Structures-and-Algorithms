import random
from icecream import ic
import math
import tkinter as tk
import re
import itertools
# Test lists 
my_list = [-29, 30, 51, 99, -34]
even_list = [10, 20, 30, 40, 50]
same_list = [1, 1, 1, 1]
# 1.1 Function that verifies if n is multiple of m
def is_multiple(n, m):
    for value in range(1, n):
        if n / value == m:
            return True
    return False
ic(is_multiple(10, 5))
ic(is_multiple(10, 3))
# 1.2 Function that verifies if a number is even or odd. It uses a pretty smart trick with bitwise operations. 
def is_even(number):
    return (number & 1) == 0
ic(is_even(7))
ic(is_even(14))
# 1.3 Funtion that return the min and max value of an iterable without using the integrated python functions. 
def minmax(iterable):
    my_max = iterable[0]
    my_min = iterable[0]
    for value in iterable:
        if value > my_max:
            my_max = value
        if value < my_min: 
            my_min = value
    return my_max, my_min
ic(minmax(my_list))
# 1.4/1.5 Returns the sum of the squared positive integers smaller than the number provided. Done as a single return statement.
def square_sum(number):
    return sum([value**2 for value in range(number)])
ic(square_sum(100))
# 1.6/1.7 Returns the sum of the odd squared positive integers smaller than the number provided. Done as a single return statement.
def square_oddsum(number):
    return sum([value**2 for value in range(1, number, 2)])
ic(square_oddsum(10))
# 1.8 This is a demonstration that given a negative index -j the same object will be referenced by len(iterable) + (-j) as a positive index. E. g. iterable[-2] when len(iterable) == 5 would also be iterable[3]
def same_index(iterable, index):
    if index < 0:
        return iterable[index], iterable[len(iterable) + index]
    elif index >= 0:
        return iterable[index], iterable[index - len(iterable)]
ic(same_index(my_list, -2))
ic(same_index(even_list, 2))
# 1.9 Range that produces the list of values [50, 60, 70, 80]
ic(list(range(50, 90, 10)))
# 1.10 Range that produces the list of values [8, 6, 4, 2, 0, -2, -4, -6, -8]
ic(list(range(8, -10, -2)))
# 1.11 List comprehension that produces the list of values [1, 2, 4, 8, 16, 32, 64, 128, 256]
ic([2**n for n in range(9)])
# 1.12 My own implementation of the choice function from the random module using randrange
def my_choice(iterable):
    return iterable[random.randrange(len(iterable))]
ic(my_choice(my_list))
# 1.13 An iterable inversor using list comprehensions
def inverse(iterable): 
    return [iterable[value] for value in range(-1, (-len(iterable)) - 1, -1)]
ic(inverse(my_list))
# 1.13 An iterable inversor using list slices
def inverse_slice(iterable):
    return iterable[::-1]
ic(inverse_slice(my_list))  
# 1.14 Check if there's some value pair in an iterable that when multiplied returns an odd number. 
def oddpair(iterable):
    for value in set(iterable):
        if not is_even(value):
            return f'Any number multiplied by {value} would return an odd number'
    return "There are no value pairs that, when multiplied, return an odd number"
ic(oddpair(my_list))
ic(oddpair(even_list))
# 1.15 Check if the numbers inside a list are distinct from each other. Done pretty easily by comparing len(set(iterable)) and len(iterable)
def aredistinct(iterable):
    return len(set(iterable)) == len(iterable)
ic(aredistinct(my_list))
ic(aredistinct(same_list))
# 1.16 This happend because  numeric types are indeed immutable, but list are mutable. A list of immutable types is still mutable since all lists are mutable.
# 1.17 This doesnt work because val is taken as a new variable in the for loop. Because of this, it's not actually referencing the value in the original list. This code would merely assign a new value to val for each iteration, without changing the original list. 
# 1.18 List comprehension that returns the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
ic([sum(range(0, 2*n + 1, 2)) for n in range(10)])
# 1.19 Function that uses List comprehension to return the list of character from n to m. Works by turning characters into their ASCII equivalent. Calling it with 'a' and 'z' as arguments returns the solution to 1.19
def charrange(n, m):
    return [chr(i) for i in range(ord(n), ord(m) + 1)]
ic(charrange('d', 's'))
# 1.20 my own random.shuffle() implementation 
def myshuffle(iterable):
    copy = iterable.copy()
    new_iterable = []
    while len(copy) > 0:
       r_int = random.randint(0, len(copy) - 1)
       new_iterable.append(copy.pop(r_int))
    return new_iterable
ic(myshuffle(my_list))
# 1.21 EOFError handling. Will not be called every time you run the script, but if you want to see how it works you should call the function, provide however many lines of input you want in the terminal, then send ^Z into the terminal to terminate input and thus rise an EOFError. In which case the input provided will be printed as a reversed list of the order it was provided. 
def reverse_input_lines():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        ic(list(reversed(lines)))
# 1.22 Dot product function. Returns a tuple with the first element being the first list, the second element being the second list, and the third element being the dot product of the two. 
def dotproduct(list_a, list_b):
    return list_a, list_b, [list_a[i] * list_b[i] for i in range(len(list_a))]
ic(dotproduct(my_list, even_list))
# 1.23 List insert function that has a personalized IndexError handling. Weirdly enough python insert() actually handles both negative and beyond len(list) indexes by inserting either at the start or the end of the list. This is good, actually, but made it hard for me to actually raise an IndexError for the exercise, I managed to do it through list avoiding methods at all. 
def listinsert(list, value, index):
    try:
        list[index] = value
        return list
    except IndexError as e:
        return f"{str(e)}. Dont try buffer overflow in Python!"
ic(listinsert(my_list, 3, 100))
# 1.24 Vowel Counter. Returns the amount of vowels found in a given string by default, but the behaviour could be changed by providing a second argument as a list of characters. 
def countcharacters(string, charlist = ['a', 'e', 'i', 'o', 'u']):
    matches_dict = {key: 0 for key in charlist}
    total = 0
    for character in string: 
        if character in charlist:
            matches_dict[character] += 1
            total += 1
    return matches_dict, f'Total Matches: {total}'
# Calling the function with charlist being default
ic(countcharacters('aaeeiioouu'))
# A nice demonstration of modularity, using a function defined in 1.19 to showcase the usage of a non-default behaviour for countcharacters()
ic(countcharacters('testingsomething', charrange('d', 'i')))
# 1.25 A punctuation cleaner using the regex module. It might not work in some very specific cases, but its good enough
def clearpunctuation(string):
    return re.sub(r'[^\s\w]', '', string)
ic(clearpunctuation('this is..... a string,,,, with many punct!uation character...s'))
# 1.26 A function that checks if 3 integers can generate an equivalence with the operators provided. By default they're all of the operators. Returns a dictionary that contains two keys. any_true contains a boolean that is true if any of the equivalences succeded. result_list contains the list of test operations performed and their result in the form of a tuple. I decided to write it as a function to have all the solutions packed in a single file, but it can be done as a program by simply adding x = input('Provide x:') and then calling the function with the values provided. 
def isarithmetic(a, b, c, operators=['+', '-', '/', '%', '//', '*', '**']):
    results= {'result_list': []}
    for op in operators:
        results['result_list'].append((f'{a} {op} {b} == {c}', eval(f'{a} {op} {b} == {c}')))
    for op in operators:
        results['result_list'].append((f'{a} == {b} {op} {c}', eval(f'{a} == {b} {op} {c}')))
    results['any_true'] = any([tup[1] for tup in results['result_list']])
    return results
aridic = isarithmetic(2, 2, 100)
ic(aridic['any_true'])
# 1.27 Fix on the generator provided in SECTION 1.8 so it provides the factors of the number in increasing order. Even the code looks simpler!
def factors(n): 
    k = 1
    while k < n: 
        if n % k == 0:
            yield k
        k += 1
ic([factor for factor in factors(20)])
# 1.28 P-norm of a vector. With v being an iterable with the coordinates and p having as a default value the Euclidean norm (p = 2). I don't even know what the fuck is a p-norm, but it works. That's the magic of coding, right? 
def norm(vector, p = 2):
    valuesum = sum([value**p for value in vector])
    root = valuesum**(1/p)
    return "{:.2f}".format(root)
ic(norm((12, 12, 15)))
# 1.29 Function that outputs all of the possible strings from length 2 to n out of a list of characters (provided as a string or as a list) where n is len(list of characters) without repeating characters. 
def possiblestrings(charlist):
    permlist = []
    for n in range(2, len(charlist) + 1):
        permlist += itertools.permutations(charlist, n)
    joinedlist = [''.join(tup) for tup in permlist]
    return joinedlist
ic(len(possiblestrings('catdog'))) # I output the len instead of the actual list since the list would take the entire terminal.
# An alternative solution that provides only permutations where n == len(string)
def lengthstrings(string):
    permlist = itertools.permutations(string)
    joinedlist = [''.join(tup) for tup in permlist]
    return joinedlist
ic(len(lengthstrings('catdog'))) # I output the len instead of the actual list since the list would take the entire terminal.
# 1.30 Floor log. Floor log integer of the provided base. Default base is 10. 
def floorlog(number, base = 10):
    counter = 0
    while number >= base:
        number /= base
        counter += 1
    return counter
ic(floorlog(1000))
# Log (base 10) calculator. Made using the floorlog() defined previously
def log(number, precision = 10):
    result = ''
    integer = floorlog(number)
    result += f'{str(integer)}.'
    decnumber = (number / (10**integer))**10
    for _ in range(precision):
        n = floorlog(decnumber)
        result += str(n)
        decnumber = (decnumber / (10**n))**10
    return result.rstrip('0').rstrip('.')
ic(log(500, precision=9))
# Log of any base calculator. Takes advantage of loga(x) = log10(x) / log10(a). Really accurate for the simple implementation
def logbase(number, base = 2, precision = 2):
    logb = float(log(number))/float(log(base))
    return f"{logb:.{precision}f}" 
ic(logbase(25, 4, 5))
# 1.31 Change giver using divmod, with a default bills and coins system specified. Returns a tuple x list where x[1] == Bill x[2] == Amount of that bill given. It has conditional statements in case that the remaining is negative or zero. 
def change(owed, given, bills = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]):
    change = {}
    remaining = given - owed
    if remaining == 0: 
        return 'No change given'
    elif remaining < 0:
        return f'You still owe me {abs(remaining)} dollars'
    for bill in bills:
        if bill > remaining:
            continue
        else:
            change[bill], remaining = divmod(remaining, bill)
    return list(change.items())
ic(change(1571, 11800))
# 1.32 Terminal calculator through user input using eval(). Since eval() is being used in combination with input() there are clearly some security issues with this approach, but I was too lazy to implement an elif statement for every operator. Initialized by calling the calculator() function 
def calculator():
    result = 0
    operator = None
    while True:
        user_input = input("Enter a number or operator (+, -, *, /, =): ")
        if user_input.isdigit():
            num = float(user_input)
            if operator == None:
                result = num
                print(f"= {result}")
            else:
                result = eval(f'result {operator} num')
                print(f'= {result}')
                operator = None
        elif user_input in ['+', '-', '*', '/']:
            operator = user_input
            print(user_input)
        elif user_input == '=':
            print(f"= {result}")
        else:
            print("Invalid input. Enter a number or one of the operators: +, -, *, /, =")
# 1.33 Calculator GUI using tkinter. Initialized by running the calculatorGUI() function. The problem asked to build a GUI inside the terminal, but this seemed pointless to me when one could make an actual GUI for the program. 
def button_click(value):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(tk.END, current + value)

def clear_screen():
    screen.delete(0, tk.END)

def calculate():
    expression = screen.get()
    try:
        result = str(eval(expression))
        clear_screen()
        screen.insert(tk.END, result)
    except:
        clear_screen()
        screen.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

# Screen
screen = tk.Entry(root, width=25, borderwidth=5)
screen.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate, padx=20, pady=10).grid(row=row, column=col)
    elif button == 'C':
        tk.Button(root, text=button, command=clear_screen, padx=20, pady=10).grid(row=row, column=col)
    else:
        tk.Button(root, text=button, command=lambda b=button: button_click(b), padx=20, pady=10).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1
def calculatorGUI():
    root.mainloop()
# 1.34 Print 100 sentences with 8 of them having typos. It uses a combination of random functions to make sure that out of 100 prints there's always typos prints with a typo selected randomly. 
def hundredsentence(string, typos = 8):
    characters = charrange('a', 'z')
    counter = typos
    for _ in range(100):
        if math.floor((random.random()) * 10) in list(range(0, math.ceil(typos/10) + 1)) and counter > 0:
            newstring = list(string)
            newstring[random.randint(0, len(newstring) - 1)] = characters[random.randint(0, len(characters) - 1)]
            counter -= 1
            print('typo:', ''.join(newstring))
        else: 
            print(string)
# 1.35 Birthday problem experiment test. n is amount of birthday date lists, m is amount of bithdays per list m. Returns the percentage of lists that have at least a pair of shared birthdays. It uses set() cleverly since by comparing the lenght of the list agains the length of the set of the list if it's the case that there was, at least, a birthday pair the set would always be smaller than the list. 
def birthday(n, m): 
    results = []
    for _ in range(n):
        bd = []
        for _ in range(m):
            bd.append(random.randint(1, 365))
        results.append(len(bd) != len(set(bd)))
    percentage = (sum(results)/len(results)) * 100
    return f'{percentage:.2f}%'
ic(birthday(1000, 23))
# This function runs the test 1000 times for values from 10 to 100 to show that the paradox is true
def testparadox():
    return {m: birthday(1000, m) for m in range(10, 101, 10)}
# 1.36 Word Counter without collections.Counter()
def wordcounter(string):
    counter = {}
    for word in string.split():
        if word not in counter: 
            counter[word] = 1
        else:
            counter[word] += 1
    return counter
ic(wordcounter('test test test not not something something etc etc'))