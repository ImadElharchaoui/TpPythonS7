from EX3 import read_file
from EX9 import get_positive_integer


try:
    filename = input("Enter the file name: ")
    content = read_file(filename)
    print("File content:", content)

    number = get_positive_integer()
    print(f"Valid number entered: {number}")

except Exception as e:
    print(f"Unexpected error: {e}")


