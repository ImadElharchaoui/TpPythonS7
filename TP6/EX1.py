def safe_division(a, b):
    if b == 0:
        raise ZeroDivisionError("Division sur 0 immposible.")
    return a / b


try:
    print(safe_division(10, 2))  
    print(safe_division(10, 0))  
except ZeroDivisionError as e:
    print(f"Error: {e}")
