class NegativeAgeError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")
    print(f"Age est: {age}.")


try:
    set_age(21)
    set_age(-555) 
except NegativeAgeError as e:
    print(f"Error: {e}")
