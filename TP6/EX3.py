def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: fichier '{filename}' n'existe pas.")
    finally:
        print("fichier fermer.")


print(read_file("existing_file.txt"))
print(read_file("nonexistent.txt"))
