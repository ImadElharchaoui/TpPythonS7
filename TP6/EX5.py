def process_input(user_input):
    try:
        value = int(user_input)
        result = 10 / value
        print(f"Result: {result}")
    except ValueError:
        print("Error: Input n'est pas entier.")
    except ZeroDivisionError:
        print("Error: Division sur 0 immpossible .")


process_input("10")
process_input("Imad")
process_input("0")
