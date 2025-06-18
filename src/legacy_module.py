# src/legacy_module.py

# Simulating a large function with global variables
global_variable = 100

def legacy_function():
    global global_variable
    try:
        result = global_variable * 2
        # Simulating a big block of outdated code
        if result > 100:
            print "The result is larger than 100"
            return result
        else:
            raise ValueError("The result is too small")
    except ValueError, e:
        print "Error:", e
        return None

def another_legacy_function(data):
    if data > 50:
        return legacy_function()
    else:
        return "Data too small"
