
1. Class 

A class is a blueprint for creating objects.

class Mobile:
    pass
# the function the class that will be present in class will be here

    
2. Object 📱

An object is an instance of a class.

m1 = Mobile()
m2 = Mobile()

# call the function of call in form of name 

Each object is different.



3. Attributes 📦

Attributes store data inside an object.
# calling the features in form of attribute as 

self.brand
self.price

Example:

m1.brand = "Orange"


4. __init__() ⚙️

A special method that runs automatically when an object is created.

def __init__(self, brand, price):

Its job is to initialize the object.

# use for creating a function that can run without even if the object is absent with predefined value




5. self 👤

# name of object that represent the data in it

This was today's most important concept.

Think:

self = "the current object"

Examples:

m1 = Mobile(...)

Inside __init__():

self → m1

Later,

m2 = Mobile(...)

Inside __init__():

self → m2

The same method works for different objects because self changes automatically.



6. Methods 🛠️

A method is a function inside a class.

def display(self):
    print(self.name)

Call it like:

b1.display()

Python automatically passes:

self = b1



7. Each Object Has Its Own Data
b1.balance = 65

does not change:

b2.balance

because they are different objects.

🧠 Memory Trick

Whenever you see:

self.something

Read it as:

"This object's something."

For example:

self.balance

means:
 self = object

"The balance belonging to this object."

This simple way of reading self will make OOP much easier.
