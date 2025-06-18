global_variable = 100

def legacy_function() -> int | None:
    try:
        result = global_variable * 2
        if result > 100:
            print(f"The result is larger than {result}")
            return result
        else:
            raise ValueError("The result is too small")
    except ValueError as e:
        print(f"Error: {e}")
        return None

def another_legacy_function(data: int) -> int | str:
    if data > 50:
        return legacy_function()
    else:
        return "Data too small"