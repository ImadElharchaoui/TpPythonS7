def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"'{value}' est n'est pas integer.")

# Example usage
try:
    print(convert_to_int("42")) 
    print(convert_to_int("Imad")) 
except ValueError as e:
    print(f"Error: {e}")
