
num1 = 42                                                                           #variable declaration, number
num2 = 2.3                                                                          #variable declaration, float
boolean = True                                                                      #variable declaration, boolean
string = 'Hello World'                                                              #variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']          #list, initialize
person = {                                                                          #dictionary, initialize
    'name': 'John', 
    'location': 'Salt Lake', 
    'age': 37, 'is_balding': False
    }                                                                               
fruit = ('blueberry', 'strawberry', 'banana')                                       #tuples, initialize
print(type(fruit))                                                                  #log statement, type check
print(pizza_toppings[1])                                                            #log statement, list, access value >>> Sausage
pizza_toppings.append('Mushrooms')                                                  #list, add value (push)
print(person['name'])                                                               #log statement, dictionary, access value
person['name'] = 'George'                                                           #dictionary, change value
person['eye_color'] = 'blue'                                                        #dictionary, change value
print(fruit[2])                                                                     #log statment, tuples, access value

if num1 > 45:                                                                       #if statement                                            
    print("It's greater")                                                           #log statement
else:                                                                               #else statement
    print("It's lower")                                                             #log statement, >>> It's lower

if len(string) < 5:                                                                 #if statement, length check
    print("It's a short word!")                                                     #log statement
elif len(string) > 15:                                                              #else if statment, length check 
    print("It's a long word!")                                                      #log statement
else:                                                                               #else statment
    print("Just right!")                                                            #log statement, >>> Just right!

for x in range(5):                                                                  #for loop, start = 0, end = 5
    print(x)                                                                        #log statement
""" output
>>> 0
>>> 1 
>>> 2
>>> 3
>>> 4
"""

for x in range(2,5):                                                                #for loop, start = 2, end = 5
    print(x)                                                                        #log statment
""" output
>>> 2
>>> 3
>>> 4
"""

for x in range(2,10,3):                                                             #for loop, start = 2, end = 10, increment = 3
    print(x)                                                                        #log statment
""" output
>>> 3
>>> 6
>>> 9
"""

x = 0                                                                               #while loop, variable declaration, number
while(x < 5):                                                                       #while loop, start = x (0), end = 5
    print(x)                                                                        #print statement
    x += 1                                                                          #while loop

pizza_toppings.pop()                                                                #list, delete value
pizza_toppings.pop(1)                                                               #list, delete value, index 1

print(person)                                                                       #log statement, list
person.pop('eye_color')                                                             #list, delete value
print(person)                                                                       #log statement

for topping in pizza_toppings:                                                      #for loop, each element in list
    if topping == 'Pepperoni':                                                      #if statement
        continue                                                                    #for loop, continue
    print('After 1st if statement')                                                 #log statement
    if topping == 'Olives':                                                         #if statement
        break                                                                       #for loop, break

def print_hello_ten_times():                                                        #function declared
    for num in range(10):                                                           #for loop, start = 0, end = 10
        print(f'{num}Hello')                                                              #log statement

print_hello_ten_times()                                                             #function called
"""
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
"""

def print_hello_x_times(x):                                                         #function declared, parameter = x
    for num in range(x):                                                            #for loop, start = 0, end = x 
        print(f'{num}Hello')                                                              #log statement

print_hello_x_times(4)                                                              #function called, argument = 4
"""
>>> Hello
>>> Hello
>>> Hello
>>> Hello
"""

def print_hello_x_or_ten_times(x = 10):                                             #function declared, parameter = x (default 10)
    for num in range(x):                                                            #for loop, start = 0, end = 10
        print(f'{num}Hello')                                                              #log statement

print_hello_x_or_ten_times()                                                        #function called
"""
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
>>> Hello
"""                                        
print_hello_x_or_ten_times(4)                                                       #function called, argument = 4
"""
>>> Hello
>>> Hello
>>> Hello
>>> Hello
"""

"""
Bonus section
"""

# print(num3)  - NameError: name <variable name> is not defined
# num3 = 72   
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean)  - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'