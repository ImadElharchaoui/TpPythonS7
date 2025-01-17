def safe_division_with_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division sur 0 impossible.")
    else:
        print(f"Division possible et res: {result}")
    finally:
        print("division completed.")

safe_division_with_else(10, 2)  
safe_division_with_else(10, 0)  
