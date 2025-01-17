import csv

with open("TP5/contacts.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Nom: {row['Nom']}, Age: {row['Age']}, Ville: {row['Ville']}")
