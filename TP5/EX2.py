lines = [input(f"Enter Lines {i+1}: ") for i in range(3)]

with open("TP5/phrases.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
1