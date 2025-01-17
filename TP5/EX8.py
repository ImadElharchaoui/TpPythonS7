try:
    with open("inexistant.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: il n'y a pas de file:inexistant.txt .")
