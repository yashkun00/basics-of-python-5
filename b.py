# basics-of-python-5

1. Class 🏗️

A class is a blueprint for creating objects.

class Mobile:
    pass

    
2. Object 📱

An object is an instance of a class.

m1 = Mobile()
m2 = Mobile()

Each object is different.



3. Attributes 📦

Attributes store data inside an object.

self.brand
self.price

Example:

m1.brand = "Apple"


4. __init__() ⚙️

A special method that runs automatically when an object is created.

def __init__(self, brand, price):

Its job is to initialize the object.




5. self 👤

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
b1.balance = 7000

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

"The balance belonging to this object."

This simple way of reading self will make OOP much easier.
