import math

# addition
def add(num1, num2):
    return num1 + num2

# substraction
def sub(num1, num2):
    return num1 - num2

# multiplication
def mul(num1, num2):
    return num1 * num2

# division
def div(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 / num2

# square root
def square_root(x):
    return math.sqrt(x)

# sin(a) + cos(b)
def trig(a, b):
    return math.sin(a) + math.cos(b)

print(add(2, 3))
print(sub(5, 3))
print(mul(4, 2))
print(div(4, 2))
print(square_root(4))
print(trig(3, 4))
