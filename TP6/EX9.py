def get_positive_integer():
    while True:
        try:
            value = int(input("Enter a positive integer: "))
            if value <= 0:
                raise ValueError("ur integer n'est pas positive.")
            return value
        except ValueError as e:
            print(f"Error: {e}. retrnter.")

pInteger = get_positive_integer()
print(f"Positive integer: {pInteger}")
