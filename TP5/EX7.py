import os

with open("TP5/journal.txt", "r") as file:
    with open("TP5/journal_copy.txt", "w") as copy:
        for line in file:
            copy.write(line)


os.replace("TP5/journal_copy.txt", "TP5/archives/journal_copy.txt")
        