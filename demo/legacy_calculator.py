from typing import Optional

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Optional[float]:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main() -> None:
    a = 10
    b = 5
    print(f"Performing calculations on {a} and {b}")
    
    print(f"Addition Result: {add(a, b)}")
    
    print(f"Subtraction Result: {subtract(a, b)}")
    
    print(f"Multiplication Result: {multiply(a, b)}")
    
    try:
        print(f"Division Result: {divide(a, b)}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()