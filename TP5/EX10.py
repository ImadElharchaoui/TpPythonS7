import csv

fichier  = "TP5/contacts.csv"
def ajouter_contact():
    with open(fichier, "a", newline="") as file:
        writer = csv.writer(file)
        name = input("Name: ")
        age = input("Age: ")
        city = input("City: ")
        writer.writerow([name, age, city])


def afficher_contacts():
    with open(fichier, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def recherche_contact():
    name = input("Enter name pour recherche ")
    with open(fichier, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name:
                print(row)


while True:
    choice = input("1. ajouter\n2. afficher\n3. recherche\n4. Exit\n")
    if choice == "1":
        ajouter_contact()
    elif choice == "2":
        afficher_contacts()
    elif choice == "3":
        recherche_contact()
    elif choice == "4":
        break
    else:
        print("Re-enter choice")
