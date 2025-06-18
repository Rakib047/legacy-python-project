from typing import Optional

def greet_user(name: str) -> None:
    print(f"Hello, {name}! Welcome back!")

def safe_divide(a: float, b: float) -> Optional[float]:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

def legacy_data_transform(data: list[str]) -> list[str]:
    return [item.lower() for item in data]