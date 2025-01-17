import logging

logging.basicConfig(filename="TP6/error.log", level=logging.ERROR)


def read_file_with_logging(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"File '{filename}' not found.")
        print(f"Error: fichier '{filename}' n'est pas existe.")

read_file_with_logging("nonexistent.txt")
