#This code demonstrates how to convert between different types in Python.
#Type conversion is the process of converting a value from one type to another .
#There are two types of type conversion in Python:
#1. Implicit Type Conversion: Python automatically converts one data type to another without any explicit instruction from the user.
#2. Explicit Type Conversion: The user converts one data type to another using built-in functions.
# Implicit Type Conversion
'''
a = 10        # Integer
b = 3.14      # Float
sum = a + b    # Implicitly converts 'a' to float
print(f"Implicit Type Conversion: {sum} (Type: {type(sum)})")

# Type casting 
a, b = 1, "2"
c=int(b)  # Explicitly converting string 'b' to integer
d = a + c  # Now both are integers
print(d)  # Output: 3
print(type(d))  # Output: <class 'int'>
'''
a =3.14
a=str(a)  # Explicitly converting float 'a' to string
print(a)  # Output: '3.14'
print(type(a))  # Output: <class 'str'>
