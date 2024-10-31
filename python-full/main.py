# use dir() and help() in print statement to get supported functions


"""
1  how to print a line

print (" I like pizza")

# use.strip() method to remove whitespaces

2 variable name
 
first_name = "Mohamed"
age = 22
height = 175.8
print(first_name)
print(age,height)

"String" - it is String
25 - integer 2.5 - float
{} - called place holder

3 f-string and place holder

first_name = "Mohamed"
food_name = "Parotta"
print(f"Hello {first_name}," "\n" f"You like {food_name}")

4. Boolean(True or False)

student = False
if student:
    print("I am a student")
else:
    print("No I am not a student")
print(f"Are you a student: {student}" )   

5. Typecasting(converting one data type to another)
use :- str() float() int() bool()

name = "Mohamed Aflal"
age = 21
height = 175.8
student = True
print(type(student)) #finding the type
age = str(age) #converting a type
print(age)

6. how to enter data(by user) 
use :- input()

n = input("What is your name? ") #getting input from the user
age = int(input("What is your age? ")) #converting string to integer
# age = int(age) you can use this also
age = age+1
print(f"Hello! {n}." f"Your age is {age}")

7. Finding area of circle

radius = int(input("Enter the Radius: "))
pi = 3.14
area_of_circle = pi*radius**2
print(f"Area of circle = {area_of_circle}cmB2") 

8. Shopping program

pizza_prize = 9.99
burger_prize = 7.99
sandwich_prize = 4.99

item = str(input("What item you want to buy (pizza, burger, sandwich): ").lower())

if item == "pizza":
    pizza_quantity = int(input("How many pizza you want: "))
    price = pizza_quantity * pizza_prize
    print(f"Your bought {pizza_quantity} pizza")
    print (f"Your total is ${price}")
elif item == "burger":
    burger_quantity = int(input("How many burger you want: "))
    price = burger_quantity * burger_prize
    print(f"Your bought {burger_quantity} burger")
    print (f"Your total is ${price}")
elif item == "sandwich":
    sandwich_quantity = int(input("How many sandwich you want: "))
    price = sandwich_quantity * sandwich_prize
    print(f"Your bought {sandwich_quantity} sandwich")
    print (f"Your total is ${price}")
else:
    print("We don't have the item, Sorry for inconvenience.")
    
9. madlibs game

adj = input("Enter a adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
print(f"Today I went to {adj} {noun} and was {verb}")

10. arithmetic operators
 
a = 8 
b = 9
print("addition = ",a+b)
print("subraction = ",a-b)
print("multiplication = ",a*b)
print("division = ",a/b)
print("power = ",a**2)
print("modulus = ",b%2)(checks remainder)

11. assignment operators

a = 5
a+=1 #also a = a + 1 incrment
a-=1 #also a = a - 1 decrement
a *=3 # also a = a * 3 
a /=3 #also a = a / 3 
print(a)

12. Math functions

a = 69.99
b = -80
c = 96
r1 = round(a) #rounds the value to nearest integer
r2 = abs(b) #calculates absalute value
r3 = pow(2, 8) #to calculate power
r4 = max(a,b,c) # to find maximum value
r5 = min(a,b,c) # to find minimum value
print(r1,r2,r3,r4,r5)

13. more math functions

import math #for math functions
x = 16
c = 9.16
d = 9.99
print(math.ceil(c)) #rounds to highest value
print(math.floor(d)) #rounds to lowest value
print(round(math.sqrt(x))) #prints sqrt of a var
print(math.e) #prints e value
print(math.pi) #prints pi value

14. Circumference and area of circle

import math
radius = float(input("Enter the radius: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)
print(f"circumference = {round(circumference, 3)}")# rounds to 3 decimal places
print(f"area = {round(area,2)}")

15. Pythagoras theorem

import math
a = float(input("Enter side A = "))
b = float(input("Enter side B = "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"C side = {c}")

16. Conditional statements

age = int(input("Enter your age: "))
if age>=18:
    print("You're eligible")
elif age<=0:
    print("NOT BORN YET")
else:
    print("You're not eligible")

x = input("Enter your response?  (y,n): ")
if x == "y":
    print("its a yes")
elif x == "n":
    print("its a no")
else:
    print("wrong response")

main = input("")
if main == "":
    print("please react")
else:
    print(main)
    
17. boolean conditions    

status = False
if not status:  #checking wether true or not
    print("Online")
else:
    print("Ofline")
    
18.Python Calculator    

num1 = float(input("Enter a number: " ))
num2 = float(input("Enter a number: " ))
operator = input("Enter what you want to calculate (add, sub, mul, div): ").lower()
if operator == "add":
    add = num1 + num2
    print(f"Result is : {add}")
elif operator == "sub":
    sub = num1 - num2
    print(f"Result is : {sub}") 
elif operator == "mul":
    mul = num1 * num2
    print(f"Result is : {mul}")
elif operator == "div":
    if num2!=0:
        div = num1 / num2
        print(f"Result is : {div}")
    else:
        print("Error it has zero")
else:
    print("Enter your values properly")
    
19.  converting units      

height = float(input("Enter your Weight: "))
unit = (input("Metre or Centimetre? (m, cm): ")).lower()
if unit == "m":
    height = height * 100
    unit = "Cm"
    print(f"Your height is: {height}{unit}")
elif unit == "cm":
    height = height / 100
    unit = "metre"
    print(f"Your height is: {height}{unit}")
else:
    print(f"Entered unit {unit} is invalid")
   
note:
cm to m (*100)
kg to lbs (*2.204)
c to fahrenheit (9 * c)/5+32
  
20. logical operator (link ,allow to calculate multiple conditions)
or - 1 condtion must be true
and - both conditions must be true
not - invert the condition
 
traffic = int(input("Enter the traffic density : "))
raining = input("Enter (true or false): ").lower() #assiging true or false with string
if raining == "true":
    raining = True # converting the string to boolean
elif raining == "false":
    raining = False
is_raining = raining #assiging that boolean to this if we want to get user value
if traffic > 50 or traffic < 0 or is_raining:
    print("Not going to office")
else:
    print("Going to office")  

21. AND  

temp = int(input("Enter the temp: "))
sunny = input("Enter (yes or no): ").lower()
if sunny == "yes":
    sunny = True
elif sunny == "no":
    sunny = False
is_sunny = sunny
if temp > 35 and is_sunny:
    print("it's too hot")
else:
    print("ok we can go")

22. NOT 

temp = int(input("Enter the temp: "))
sunny = input("Enter (yes or no): ").lower()
if sunny == "yes":
    sunny = True
elif sunny == "no":
    sunny = False
is_sunny = sunny
if temp <20 and not is_sunny:
    print("it's too cold")
else:
    print("OK")
    
23. conditional expression (one line if-else statement shortcut)
note:
if condition else Y

num = int(input(""))
result = "The greatest number" if num > 68 and 70 > num  else "Waste"
print(result)

24. different string objects

name = input()
result = len(name) #prints lenght of a name
r2 = name.find(" ") #finds character inside string
r3 = name.rfind("a") #reverse find (no result = -1)
r4 = name.capitalize() #capitalizes first word 
r5 = name.upper() # capitalizes everything
r6 = name.lower() #lowercase letters
r7 = name.isdigit() #true only if all are digits
r8 = name.isalpha() #true only is all are alphabets
r9 = name.count("a") #counts the charactere
r10 = name.replace("a","o")
print(result,"\n",r2,"\n",r3,"\n",r4,"\n",r5,"\n",r6,"\n",r7,"\n",r8,"\n",r9,"\n",r10)
print("1","2","3","4", sep = ", ") # sep = used for defining seperately

note: 
result = help(str) #can use this to know about multiple string objects
print(result)

25.problem with string objects

username = input()
if len(username) >=10:
    print("Username is invalid")
elif not username.find(" ") == -1:
    print("Username must not contain spaces")
elif username.isalpha() == 0:
    print("Username must not contain digits")
else:
    print(f"Welcome {username}")
    
26.indexing and slicing in string 
note :
[start:end:step] use this var name

user_name = "Mohamedaflal12344"
print(user_name[0]) #prints first character
print(user_name[0:5]) #prints charcter from 1st to 5th 
print(user_name[:5]) #also can use this
print(user_name[:10:2]) #prints all odd charcters
print(user_name[::2]) #all odd characters
print(user_name[3:]) #prints all from given start
print(user_name[-2]) #from last it calculates
last = user_name[-4:] #prints last four
print(last)
result = user_name[::-1] #reverse (palindrome)
print(result)

27.format specifiers

price_1 = 3.456
print(f"Price = {price_1:10}") #{x:conition}

28. while loop  prints untill condition is true. or break

name = input("Enter your name: ")
while name == "":
    print("Please enter your name to continue")
    name = input("Enter your name: ")
print(f"Welcome {name}")

bp = input("Enter your battery percentage : ")
while not bp == "x":
     print(f"Your battery is {bp}%")
     bp = input("Enter your battery percentage : ")
print("Thank you bye!")   

29. python compound interest calculator

principle = 0  
rate = 0
time = 0
while principle <= 0 :
    principle = float(input("Enter the principle amount : "))
    if principle <= 0:
        print("Enter correct value")
while rate <= 0:
    rate = float(input("Enter the interest rate : "))
    if rate <= 0:
        print("Enter correct value")
while time <= 0:
    time = float(input("Enter the time period in yrs : "))
    if time <= 0:
        print("Enter correct value")
total = principle * pow((1+rate/100),time)
print(f"Your Total is ${round(total,2)} for the time period {time} years")
compound_difference = total - principle
print(f"Your extra money earned is {round(compound_difference,2)}" )

30. for loop prints until specified condition

# note:
#  reversed() - revesrse the condition
#  continue - hides or ignores the condition
#  break - ends the condition
for i in (reversed(range (1,100+1))):#using reversed to print from back
    if i == 69:
        continue
    print (i)
    
31. time clock    

import time
timer = int(input("Enter the time in seconds: "))
for i in range(timer,0,-1):
    s = i % 60
    m = int(i / 60) % 60
    h = int(i / 3600)
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(5)
print("Time's up")

32. nested loop(loop inside loop)(used for patterns)

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol you want: ")
symbol = "*"
for i in range (4):
    for  j in range (4):
        print(symbol, end = " ")
    print()    
    
33. list[] - ordered and changeable duplicates OK
tuple( ) - ordered and unchangebele duplicates ok
set{ } - unordered and immutable add/remove ok no duplicates  
list:-
     
fruits = ["apple","zurich","banana","orange"]
fruits.append("pineapple") #adds to last of the container
fruits.remove("banana") #to remove from container
fruits.insert(2,"kiwi") #adds extra element at specific place
fruits.sort() #arranges in alphabetical order
fruits.clear() #removes everything
a=fruits.index("apple") #finds the position
fruits.pop() #removes first element
print(fruits,a)

34. SET


v = {"car","bike","lorry","lorry"} #no duplicates
v.add("cycle") #only add and remove
v.remove("bike")
v.pop()
#v.clear()
print(v)

35. tuples

v = ("car", "bike", "cycle", "lorry", "bike")
a = v.count("bike")
print(a)
print(v)
for ve in v:
    print(ve)
    
36. Shopping cart program    

vehicles = []
prices = []
total = 0
while True:
    vehicle = input("Enter the vehicle name: ")
    if vehicle.lower() == "exit":
        break
    else:
        price = float(input(f"Enter the price of {vehicle}: $"))
        vehicles.append(vehicle)
        prices.append(price)
print("------------Your cart----------- ")
for vehicle, price in zip(vehicles, prices): #two things in single use zip
    print(f"{vehicle}:${price}",end =" ""\n") 
    total = total+price
print(f"Your total is ${total:.2f}")

37. 2d list

cars = ["skoda","bmw","audi","swift"]
bikes = ["yamaha","ktm","honda","kawasaki"]
cycles = ["hercules","hero","dirtrider"]

vehicles = [cars,bikes,cycles] # we can also do like [[x],[x],[x]]

#print(vehicles[0][0]) #row #column

38. phone keypad

keypad = [["1","2","3"],["4","5","6"],["7","8","9"],["#","0","*"]]

for keys in keypad:
    for char in keys:
        print(char, end="  ")
    print()    
    
39. quiz game    

questions = ("How many elements are in the periodic table?: ",
"Which animal lays the largest eggs?: ",
"What is the most abundant gas in Earth's atmosphere?: ",
"How many bones are in the human body?: ",
"Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
("A. 206", "B. 207", "C. 208", "D. 209"),
("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C","D","A","A","B")
guesses = []
score = 0 
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter A OR B OR C OR D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1 

marks = score / len(questions) * 100 
print("---------------------------")
print("         RESULT            ")
print("---------------------------")
print(f"Your total score is {marks}%")

40.dictionary

capitals = {"USA": "Washington D.C.",
"India": "New Delhi",
"China": "Beijing",
"Russia": "Moscow"}
print(capitals.get("India")) #gets value of the key
capitals.pop("China") #removes given
capitals.update({"Australia":"Perth"}) #same as insert()
capitals.popitem() #removes recently added
key = capitals.keys() #getting key of the value
for keys in key:
    print(keys)
values = capitals.values() # prints value for the key assigned
for value in values:
    print(value)
print(capitals)

items = capitals.items() # prints all the items in the dictionary
print(items)
 
for keys, value in capitals.items():
    print(f"{keys}:{value}")
    
41.problem menu    
     
menu = {"pizza": 3.00, 
"nachos": 4.50, 
"popcorn": 6.00, 
"fries": 2.50, 
"chips": 1.00, 
"pretzel": 3.50, 
"soda": 3.00, 
"lemonade": 4.25}
cart = []
total = 0
print("--------- Menu --------")
for key, value in menu.items():
    print(f"{key:10}:${(value):.2f}")
print("-----------------------")
while True:
    food = input("select an item: ").lower()
    if food == "x":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------ Your order ------")        
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Your total is ${total:.2f}")

42. random module

import random
n = int(input())
m = int(input())
a = random.randint(n,m) #random integer
b = random.random() #print random anything 
options = ("siccers","rock","paper")
option = random.choice(options) #used for random choice
choices = random.shuffle(options) #used for shuffling 
print(option)

43. Number guessing game

import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print(f"Number guessing game")
print(f"Enter a number between ({lowest_num} - {highest_num})")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < lowest_num or guess > highest_num:
            print(f"{guess} is out of range")
            print(f"Enter a number between ({lowest_num} - {highest_num})") 
        elif guess < answer:
            print("Too low! try again")
        elif guess > answer:
            print("Too high! try again")
        else:
            print(f"Correct the answer is {answer}")
            print(f"number of guesses {guesses}")
            if guess == answer:
                break
            else:
                 continue
    else:
        print(f"{guess} is invalid guess")
        print(f"Enter a number between ({lowest_num} - {highest_num})")
        
43. rock paper scissors game

import random
options = ("rock", "paper", "scissors")
running = True
while running:
    computers_choice = random.choice(options)
    yr_choice = None 
    while yr_choice not in (options) :
        yr_choice = input("Enter your choice (rock,paper,scissors): ")
    print(f"Your choice is: {yr_choice}")
    print(f"Computer's choice is : {computers_choice}")
    if yr_choice == computers_choice:
            print("it's a draw")  
    elif yr_choice == "rock" and computers_choice == "scissors":
        print("You win")
    elif yr_choice == "paper" and computers_choice == "rock":
        print("You win")  
    elif yr_choice == "scissors" and computers_choice == "paper":
        print("You win")
    elif yr_choice == "scissors" and computers_choice == "rock":
        print("Computer wins")
    elif yr_choice == "rock" and computers_choice == "paper":
        print("Computer wins")  
    elif yr_choice == "paper" and computers_choice == "scissors":
        print("Computer wins")
    else:
        ("you lose")
    play_again = input("Do u wanna play again (y/n): ").lower( )
    if play_again == "y":
        continue
    else:
        print("Thank you meet you soon")
        break
        
44. function (block of resuable code)   
note:
use (def) and unique function name

def happy_birthday(n, g): #arguments should match 
    print(f"I am {n} aflal and {g} of all time")
happy_birthday("mohamed","greatest")
def invoice(username, amount, due_date):
    print(f"Hi {username}, you need to pay ${amount} within {due_date} ")

invoice("helenigger", 700, "january 7th")

45. return (used for ending a function , send result back to caller)

def add(x,y):
    z = x+y
    return z
print(f"the result of x+y = {add(1, 2)}")  

def name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = name(input(""),input(""))
print(f"your name is: {full_name}")

47. default arguments
positional,defaul,keyword,arbitery
note: if variables inside function has already defined values
it is called default arguments

positional arguments are parameters which defined inside fun() and op aswell
import time
def time_time(start, end = 10): #default arguments always should be after non default arguments
    for i in range(start, end+1):
        time.sleep(1)
        print(i)
    print("done")    
time_time(0, 30) 

48. keyword arguments 
note: keywords are parameters assigned for the variables inside fun(  )

def hello(first, last, initial):
    first = first.capitalize()
    last = last.capitalize()
    
    print(f"hi {initial} {first} {last}")
hello("mohamed", last="aflal",initial = "MR.")  #this keyword arguments  defining with keys

49. arbitary  *args *kwargs

def hydra(*names): #*args is defining multiple argument with single parameter
    while True:
        for name in names:
            name = input("Enter your name: ")
            print(name)
            if name == "x":
                return 
hydra()

def name(*names):
    for name in names:
        print(name, end = " ")
name("F","Mohamed","Aflal")

50. *kwargs keyword arguments (pass multiple kw arguments)

def print_address(**places):
    for place, details in places.items(): # .items() .keys() .values()
            print(f"{place:9}:{details}")
    
print_address(zip = "605602", city = "villupuram", state = "TamilNadu", country = "India")

51. *args and **kwargs in same

def details(*names, **address):
    for name in names:
        name = name.capitalize()
        print(f"{name}",end ="")
    print()  
    print(f"{address.get('city')}")
    # for places in address.values():
    #     print(places, end = " ")
details("mr.","mohamed"," aflal", city = "Chennai", state = "TamilNadu", country = "India")    

52. iterables (list, tuple, dictionaries, set, string all are iterables)
note: repeating again and again using loops

a = {1,2,3} #set
b = [1,2,3] #list
c = (1,2,3) #tuple
d = "good" #string
e = {"1":"one","2":"two",} #dict
print("---------- set ------------")    
for i in a:
    print(i)
print("---------- list------------")    
for j in b:
    print(j)
print("---------- tuple ------------")        
for k in c:
    print(k) 
print("---------- string ------------")        
for l in d:
    print(l)  
print("----------- dict-----------")        
for m, n in e.items():
    print(f"{m}:{n}")
print("----------------------")     

53. membership operators (in and not in)

word = "clashofclans"
while True:
    letter = input("Guess the secret word: ")
    if letter == "ktmrc200":
        print("You found the secret word")
        break
    elif letter in word: #this is in
        print(f"Your '{letter}' guess is correct keep trying")
    elif letter not in word: #this is not in
        print("Wrong guess")
    else:
        ("Wrong guess")
        
54. list comprehension - easy way to create list in python       

# doubles = []
# for i in range(1, 11):
#     x = i*2
#     doubles.append(x)
# print(doubles)
# we can do above program easily by
#[expression for value in iterables if condition]
#doubles = [expression for x in iterables]
doubles = [i*2 for i in range(1,11)]
print(doubles)

triples = [i*3 for i in range(1,11)]
squares = [i**2 for i in range(1,11)]
print(squares)
print(triples)

55. using string(list)
 
string = [strings.capitalize() for strings in ["bike","car","lorry"]]
print(string)

56. using conditions

names = ["ginger","apple","tomatos","carrots"]
length = [name for name in names if len(name) > 5]
print(length)

57. match case (switch case)
 
def days_of_week(day):
    match day:
        case 1 | "one":
            return "monday" 
        case 2:
            return "tuesday"  
        case 3:
            return "wednesday" 
        case 4:
            return "thursday" 
        case 5:
            return "friday" 
        case 6:
            return "saturday" 
        case 7:
            return "sunday" 
        case _:
            return "Not a valid day" 
f = input("Enter your number for a day: ")           
print(f"{days_of_week(f)}")

58. modules

print(help("modules")) #contains definition and statements

59. variable scope [LEGB]
local -> enclosed -> global  built - in

#LOCAL 
def fun1():
    a = 1+1
    print(a)
fun1()   #all things are defined inside so it is local and cannot access outside function
#enclosed
def fun1():
    x = 1
    def fun2():
        x=2
    print(x)
    fun2() #function inside function nested function
fun1()
#global
x = 100 #this is a global variable can accessed by any function
def fun1():
    print(x)
def fun2():
    print(x)
fun1()
fun2()

#built_in
from math import e #this is a built in value 
def fun():
    print(e)
fun() 

60. if__name__ == __main__: (seperate of block of code for using for many scripts)
def main():
    print("Ima")
    
if __name__ == '__main__':
    main()

60. encryption program

import random
import string
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

plain_text = input("secret message: ")
c = ""
for letter in plain_text:
    index = chars.index(letter)
    c += key[index]
print(f"encrypted: {c}") 

c = input("secret message: ")
plain_text = ""
for letter in c:
    index = key.index(letter)
    plain_text += chars[index]
print(f"decrypted: {plain_text}") 

61. hangman game

import random
words = ("apple", "orange", "banana", "coconut", "pineapple", 
         "bike", "road", "sky", "tree", "house","horse", 
         "car", "cloud", "river", "mountain", "ocean", 
         "book", "cat", "dog", "shoe", "ball", 
         "table", "chair", "computer", "phone", "lamp", 
         "window", "door", "grass", "flower", "star")


hangman_art = {0: ("   ","   ","   "), 
1: (" o ","   ","   "),
2: (" o "," | ","   "),
3: (" o ","/| ","   "),
4: (" o ","/|\\","   "),
5: (" o ","/|\\","/  "),
6: (" o ","/|\\","/ \\")}

def display_man(wrong):
    print("-----------------------")
    for line in hangman_art[wrong]:
        print(line)
    print("-----------------------")    
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)    
        if  guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong+= 1
        if "_" not in hint:    
            display_man(wrong)
            display_answer(answer)
            print("You Win!")
            is_running = False
        elif wrong >= len(hangman_art) - 1:
            display_man(wrong)
            display_answer(answer)
            print("You Lose!")
            is_running = False
        
if __name__ == '__main__':
    main()
    
62. oops concept  (class and objects) 

class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"Your car {self.model}")
        
    def stop(self):
        print(f"{self.model} stop")
        
car1 = car("tata", 2024, "red", False)
car2 = car("audi", 2019, "black", True)        
    
print(car2.color)   

car2.drive()
car2.stop()

63. class variables (variables inside class)

class student:
    
    class_year = 2025
    num_student = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_student += 1
        
student1 = student("aflal", 21)
student2 = student("naresh", 22)

print(student1.name,student1.age,student.class_year)
print(f"No. of students = {student.num_student}")

64. Inheritance

class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class dog(animal):
    def speak(self):
        print("WOOF")
class cat(animal):
     def speak(self):
        print("Meow")
class mouse(animal):
    pass
Dog = dog("Scobby")
Cat = cat("Asteriod Destroyer")
Mouse = mouse("Mickey")

print(Dog.name)
print(Dog.is_alive)
Dog.eat()
Dog.sleep()

65.multiple inheritence

class animal:   #multilevel inheritence
    def __init__(self,name):
        self.name = name
    def hunt(self):
        print(f"{self.name} is Hunting")
    def sleep(self):
        print("this animal is sleeping")
class prey(animal):
    def prey(self):
        print("The is food")
class predator(animal):  #multiple inhertence
    def predator(self):
        print("The is hunter")
    
class plants(prey):
    pass
class deer(prey, predator):
    pass
class lion(predator):
    pass
Lion = lion("Simba")
Deer = deer("Salman")
Plants = plants("Chedi")

Lion.hunt()

66. super()

class shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(F"COLOUR: {self.color} FILLED: {self.is_filled}")
        
class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
class square(shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
class rectangle(shape):
    def __init__(self, color, width, is_filled, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
        
Circle = circle(color = "pink", is_filled = True, radius = 5)
Square = square(color = "red", is_filled = False, width = 5)
Rectange = rectangle(color = "yellow", is_filled = True, width = 5, height = 2)

Square.describe()

67. polymorphism many form

from abc import ABC, abstractmethod
class shapes:
    @abstractmethod
    def area(self):
        pass
class Circle(shapes):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius **2
class Square(shapes):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side**2
class Triangle(shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5

class pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings
        
Shapes = [Circle(5),Square(4),Triangle(5, 6), pizza("peporonni", 4)]
 
for shape in Shapes:
    print(shape.area())

68.ducktyping

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")
        
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    print(Animal.alive) 
    
69. static method

class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    
    def is_valid_position(position):
        valid_position = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_position
        
employee1 = employee("Aflal","Manager")
employee2 = employee("mohamed","Cashier")
employee3 = employee("thamim","Cook")
employee4 = employee("Ansari","Janitor")


print(employee.is_valid_position("Rocket engineer"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())

70. class methods

class student:
    count = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        
    #instance method    
    def get_info(self):
        return f"{self.name} {self.gpa}"
   
    @classmethod
    def get_count(cls):
        return f"Total no of students: {cls.count}"

student1 = student("aflal","9.9")
print(student1.get_info())
print(student.get_count())

71. magic methods or dunder methods

class ipl:
    
    def __init__(self, cap, team):
        self.cap = cap
        self.team = team
        
    def __str__(self):
        return f"{self.cap} for {self.team}"
   # def __eq__(self):  used for comparing
   # def_lt__: used for lesser Than
   # def_gt__: used for greater than
    #there are many dunder like this
        
team1 = ipl("dhoni", "csk")
team2 = ipl("kohli", "rcb")
team3 = ipl("rohit", "mi")

print(team1)
print(team1 == team2)

72. property | we can add addititonal logics inside using getter, setter and deleter

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @name.deleter
    def name(self):
        del self._name


person = Person("Alice")
print(person.name)
person.name = "Bob"  # Setting the name attribute (setter)
del person.name  # Deleting the name attribute (deleter)

73. decorator

#decorator function
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles✨ *")
        func(*args, **kwargs)
    return wrapper   
    
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper    

#base function
@add_sprinkles #we are decorating our base function using decorator not modifying it
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("chocalate")

75. exception (interupts flow of a program)
(zerodivisionerror, typeerror, valueerror)

(methods - try, except, finally)
Exception:

# 1 + "1" this is a type error
# int = "Aflal" this is a value Error (int to str)
# anything cannot divided by zero (zero error)

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("Don't enter zero")
except TypeError:
    print("Entered wrong type")
except ValueError:
    print("Enter correct")
except Exception:
    print("Something went wrong")
finally: #excutes if there is exception or not
    print("do some cleanup here")

76. .join

words = ["Hello", "world"]
sentence ="-".join(words) #we can use this to join values
print(sentence)  

word1 = "hello world"

words = word1.split()
sentence = " ".join(word.capitalize() for word in words )
print(sentence)

77. file detection

import os 
file_path = "python.txt" #this is how u assign file path
if os.path.exists(file_path): #searching in os
    print("True")
else:
    print("False")

78.writing a file {.txt, .json, .csv}

txt_data = "I like pizza" #data to be written
file_path = "python.txt" #open file
with open(file_path, "w") as file: #the w represents writing u can also use a for appending
    file.write(txt_data) #writing a file
    print(f"txt file '{file_path} was created")
    
79.  csv file creation

import csv

employee = [["name","age","id"],["aflal","21","69"]]

file_path = "python.csv"
try:
    with open(file_path, "w") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("this file already exists")

80. reading files

file_path = "python.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)
 
81. date & time    
 
import datetime
date = datetime.date(2025,1,2)
today = datetime.date.today()

time = datetime.time(12,43,9)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d-%m-%Y")
print(now)

82. multithreading (multiple tasks)

import threading
import time

def task1():
    for i in range(5):
        print("Task 1:", i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2:", i)
        time.sleep(1)

if __name__ == "__main__":
    # Create thread objects
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Both tasks are done.")    

82. swapcase

x = "ABCDEFGabcdefg"
y = x.swapcase()
print(y)

83. title()

x = "hello World"
y = x.title()  #make the first character of each word to uppercase and other to lowercase
print(y)
"""





































































































































































































































