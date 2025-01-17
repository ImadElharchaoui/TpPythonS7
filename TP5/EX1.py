with open("TP5/exemple.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line}")
