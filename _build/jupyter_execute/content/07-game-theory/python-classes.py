#!/usr/bin/env python
# coding: utf-8

# # Python Classes
# 
# Because Python is an [**object-oriented** programming language](https://en.wikipedia.org/wiki/Object-oriented_programming), you can create custom structures for storing data and methods called **classes**. A class represents an object and stores variables related to and functions that operate on that object. You're already familiar with Python classes, even if you don't know it: the `Table`s you work with in Data 8 are Python classes, as are NumPy arrays.
# 
# We use classes because they allow us to store data in a rigorously structured way and provide standardized methods of accessing and interacting with that data. For example, let's say you want to create a program that manages a person's banking information. You need to store their name, account number, and balance. You might do something like create an array for each individual, where the first element is their name, the second is their account number, and the third is their balance:
# 
# ```python
# account1 = make_array("Jane Doe", 123456, 100)
# account2 = make_array("John Doe", 234567, 80)
# ```
# 
# But what happens if you need to track more data? Or suppose the structure of this data changes? Then you need to go to _every_ place where you access an element of the array and update it! It's really easy to forget things like this or to have instances fall through the cracks. Instead, we might create an `Account` class, so that whenever we need to update the structure, we need only do so once. (This is a very simplified version of a complex topic called [data abstraction](http://composingprograms.com/pages/22-data-abstraction.html) that demonstrates the need for complex, templated data structures and methods of accessing their data without violating [abstraction barriers](http://composingprograms.com/pages/22-data-abstraction.html#abstraction-barriers).)
# 
# Some terminology: a **class** is the abstract definition of one such data structure, the definition from which class instances are created. When refer to an **instance**, we mean a single copy of one of these objects. It's kind-of like cookies and cookie cutters: the class is the cookie cutter, the template from which we make instances, the cookies. Think about tables: `Table` is the class from which we create table instances:
# 
# ```python
# Table # this is the class
# tbl = Table() # this is an instance
# ```
# 
# Instances are created by calling the **constructor** (more below) as if it were a function (e.g. `Table()`).

# ## Creating Instances

# Classes can be created using a `class` statement. Inside the statement, you put the variables and methods that define the class. The first and most important of these methods is the `__init__` method which is called when an instance of a class is created. `__init__` is an example of Python's [dunder (double-underscore) methods](https://www.geeksforgeeks.org/dunder-magic-methods-python/), which are used to allow classes to interact with built-in functions and operators.
# 
# The `__init__` method should take any arguments needed for the class and create all of the _instance variables_ that the instance tracks. Consider the `Car` class:

# In[10]:


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


# Note that the first argument to the `__init__` method is a variable called `self`; this argument will be filled by Python with the instance of class that is being called. For example, when we call an instance's **method** (a function included in the class), we might have something like:
# 
# ```python
# class Foo:
#     def bar(self):
#         return None
# 
# foo = Foo()
# foo.bar()
# ```
# 
# When we run `foo.bar()`, the function `Foo.bar` is called and the first argument (`self`) is filled with the instance `foo`. 
# 
# In the `__init__` method (or any method, for that matter), we create instance variables (variables tied to a single instance of a class) using `<instance>.<variable name>` syntax, e.g.
# 
# ```python
# self.some_variable = "some value"
# ```
# 
# If we're outside of a method, we can use the same syntax using the variable name:
# 
# ```python
# foo.some_variable = "some value"
# ```
# 
# When you create a `Car`, `Car.__init__` is called by Python. We can create a `Car` and access the values of its instance variables using the dot syntax.

# In[11]:


car = Car("Honda", "Civic", 2018, "blue")
car.make


# ## Class Representations

# Now let's see what our `car` object (an instance of the `Car` class) looks like.

# In[12]:


car


# Hmm, that representation isn't very descriptive. Another dunder method of Python's is `__repr__`, which defines a string representation of an object. Let's define one for our `Car` class.

# In[13]:


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def __repr__(self):
        return self.color + " " + str(self.year) + " " +self.make + " " + self.model


# Now that we have defined `Car.__repr__`, we can get a nicer representation of `car`.

# In[14]:


car = Car("Honda", "Civic", 2018, "blue")
car


# ## Operators

# Now let's create two of the same cars and compare them. They should be equal, right...?

# In[15]:


car_1 = Car("Honda", "Civic", 2018, "blue")
car_2 = Car("Honda", "Civic", 2018, "blue")

car_1 == car_2


# They aren't equal! That's because, by default, the custom classes are only equal if they are the *same instance*, so `car_1 == car_1` is `True` but `car_1 == car_2` is `False`. For this reason, we need to define the `__eq__` dunder method of `Car` which Python will call when we use the `==` operator on a `Car`. We'll say and object is equal to a `Car` if the other object is also a `Car` (determined using the `isinstance` function) and has the same four attributes as the current car.

# In[16]:


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        
    def __repr__(self):
        return f"{self.color} {self.year} {self.make} {self.model}"
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model and                 self.year == other.year and self.color == other.color
        return False        


# Now our call from above will work:

# In[17]:


car_1 = Car("Honda", "Civic", 2018, "blue")
car_2 = Car("Honda", "Civic", 2018, "blue")

car_1 == car_2


# Other important dunder methods include
# 
# | Method Name | Description |
# |-----|-----|
# | `__str__` | the string representation of an object |
# | `__len__` | length of an object (`len(obj)` |
# | `__lt__`, `__gt__`, `__lte__`, `__gte__` | less than, greater than, less than or equal to, and greater than or equal to operators, resp. |
# | `__hash__` | [hash function](https://en.wikipedia.org/wiki/Hash_function) value (`hash(obj)`) |
# | `__getitem__`, `__setitem__` | getter and setter (resp.) for indexes (`obj[idx]`) |
# | `__getattr__`, `__setattr__` | getter and setter (resp.) for dot syntax (`obj.attr`) |
# 
# Note that when using comparison operators the object to the **left** of the operator has its comparison operator method called. In the below example, the first comparison calls `point_1.__lt__` and the second calls `point_2.__lt__`.
# 
# ```python
# point_1 = Point()
# point_2 = Point()
# 
# point_1 < point_2      # calls point_1.__lt__
# point_2 < point_1      # calls point_2.__lt__
# ```

# ## Instance Methods

# Now let's define some methods for a `Car`. We'll add a few more instance variables:
# 
# * `car.mileage` is the number of miles driven by the car
# * `car.gas` is number of gallons of gas in the tank
# * `car.mpg` is the number of miles to a gallon that the car gets.
# 
# Note that `car.mileage` and `car.gas` are initialized to 0 when we create the car in `__init__`. We'll first define the `fill_tank` method, which fills the gas tank to 10 gallons.

# In[18]:


class Car:
    def __init__(self, make, model, year, color, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mpg = mpg
        self.mileage =  0
        self.gas = 0
        
    def __repr__(self):
        return f"{self.color} {self.year} {self.make} {self.model}"
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model and                 self.year == other.year and self.color == other.color
        return False
    
    def fill_tank(self):
        self.gas = 10


# We can create a car and fill its take by calling `car.fill_tank`.

# In[19]:


car = Car("Honda", "Civic", 2018, "blue", 18)
car.fill_tank()
car.gas


# ### Assertions

# Now we'll define the `car.drive` method that drives `miles` miles and ensures that we have enough gas to drive that far by throwing an `AssertionError` if we don't. 
# 
# We throw assertion errors using an `assert` statement which takes two arguments: a boolean expression and a string telling the user what caused the error. For example, if we want to make sure that a string has no spaces, we might write
# 
# ```python
# assert " " not in string, "Spaces found in string"
# ```
# 
# Then, if `string` has a space, the user would see:

# In[20]:


string = "some string"
assert " " not in string, "Spaces found in string"


# ### Reassignment Operators

# Another new syntax needed for the `Car.drive` method is `+=` and `-=`. An operator followed by `=` tells Python to perform the operation combining the values on the left and right sides of the operator and then reassigns this value to the variable on the left side. This means that the expression `x += 2` is the exact same as `x = x + 2`.

# In[21]:


x = 2

x += 1
print(x) # x is now 3

x -= 4
print(x) # x is now -1

x *= 100
print(x) # x is now -100

x /= -100
print(x) # x is now 1


# Now let's define `Car.drive`. 

# In[22]:


class Car:
    def __init__(self, make, model, year, color, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mpg = mpg
        self.mileage =  0
        self.gas = 0
        
    def __repr__(self):
        return f"{self.color} {self.year} {self.make} {self.model}"
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model and                 self.year == other.year and self.color == other.color
        return False
    
    def fill_tank(self):
        self.gas = 10
        
    def drive(self, miles):
        assert miles <= self.gas * self.mpg, f"not enough gas to drive {self.miles} miles"
        self.mileage += miles
        self.gas -= miles / self.mpg


# Let's drive our `Car` 100 miles.

# In[23]:


car = Car("Honda", "Civic", 2018, "blue", 18)
car.fill_tank()
car.drive(100)
car.mileage, car.gas


# Now let's see how many miles we have left to drive by defining `Car.miles_to_empty`.

# In[24]:


class Car:
    def __init__(self, make, model, year, color, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mpg = mpg
        self.mileage =  0
        self.gas = 0
        
    def __repr__(self):
        return f"{self.color} {self.year} {self.make} {self.model}"
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.make == other.make and self.model == other.model and                 self.year == other.year and self.color == other.color
        return False
    
    def fill_tank(self):
        self.gas = 10
        
    def drive(self, miles):
        assert miles <= self.gas * self.mpg, f"not enough gas to drive {self.mileage} miles"
        self.mileage += miles
        self.gas -= miles / self.mpg
        
    def miles_to_empty(self):
        return self.gas * self.mpg
    
car = Car("Honda", "Civic", 2018, "blue", 18)
car.fill_tank()
car.drive(100)
car.miles_to_empty()


# We have 80 miles left before we're empty, so we see that if we try to drive 90 miles, the car will thrown an error:

# In[25]:


car.drive(90)


# For more information on Python classes, check out [Sections 2.5-2.7 of Composing Programs](http://composingprograms.com/pages/25-object-oriented-programming.html), the CS 61A/CS 88 textbook.

#  
