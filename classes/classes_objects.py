# Python Classes/Objects

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class

# To create a class, use the keyword class:
# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5

# Create Object

# Now we can use the class named MyClass to create objects:
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

# Delete Objects

# You can delete objects by using the del keyword:
# Delete the p1 object:
del p1

# Multiple Objects

# You can create multiple objects from the same class:
# Create three objects from the MyClass class:
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Note: Each object is independent and has its own copy of the class properties.

# The pass Statement

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass

# Create a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

# Create an object
p1 = Person("John", 36)

# Call the greet method
p1.greet()
