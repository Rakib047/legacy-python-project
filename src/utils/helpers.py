# src/utils/helpers.py

# Python 2.x-style string formatting
def greet_user(name):
    print "Hello, %s! Welcome back!" % name

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError, e:
        print "Cannot divide by zero!"
        return None

# Legacy data transformation
def legacy_data_transform(data):
    result = []
    for item in data:
        result.append(item.lower())
    return result
