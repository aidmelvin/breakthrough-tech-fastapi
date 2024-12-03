# python_intro.py

# Introduction to basic data types
print("Python Basic Data Types")

# Integer
age = 25
print(f"age: {age}, type: {type(age)}")

# Float
height = 5.9
print(f"height: {height}, type: {type(height)}")

# Boolean
is_active = True
print(f"is_active: {is_active}, type: {type(is_active)}")

# String
name = "Alice"
print(f"name: {name}, type: {type(name)}")

# List (Array-like structure)
fruits = ["apple", "banana", "cherry"]
print(f"fruits: {fruits}, type: {type(fruits)}")

# Tuple (Immutable list)
coordinates = (10, 20)
print(f"coordinates: {coordinates}, type: {type(coordinates)}")

# Dictionary (Key-value pairs)
person = {
    "name": "Bob",
    "age": 30,
    "is_active": False
}
print(f"person: {person}, type: {type(person)}")

# Set (Unique values, unordered)
unique_numbers = {1, 2, 3, 3}
print(f"unique_numbers: {unique_numbers}, type: {type(unique_numbers)}")

# Functions
def greet(name):
    return f"Hello, {name}!"

greeting_message = greet("Charlie")
print(f"greeting_message: {greeting_message}")

# Classes and Objects
class Todo:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    
    def __repr__(self):
        return f"Todo(title={self.title}, description={self.description})"

# Creating an object of the Todo class
todo1 = Todo("Learn Python", "Complete the Python course")
print(todo1)

# Creating a list of Todo objects
todos = [
    Todo("Learn Python", "Complete the Python course"),
    Todo("Build a project", "Create a simple Python app"),
]

print(f"All Todos: {todos}")
