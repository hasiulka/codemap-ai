def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b):
    sum_result = add(a, b)
    product_result = multiply(a, b)
    return sum_result, product_result

def subtract(a, b):
    return a - b

def divide(a, b):
    if b != 0:
        return a / b
    return None

def advanced_calculate(a, b):
    total, product = calculate(a, b)
    difference = subtract(a, b)
    quotient = divide(a, b)
    return total, product, difference, quotient
