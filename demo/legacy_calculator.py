# legacy_calculator.py

# Old-style print and exception handling
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError, e:
        print "Error: Cannot divide by zero!"
        return None

def main():
    a = 10
    b = 5
    print "Performing calculations on %d and %d" % (a, b)
    
    result = add(a, b)
    print "Addition Result: %d" % result
    
    result = subtract(a, b)
    print "Subtraction Result: %d" % result
    
    result = multiply(a, b)
    print "Multiplication Result: %d" % result
    
    result = divide(a, b)
    if result:
        print "Division Result: %f" % result

if __name__ == "__main__":
    main()
