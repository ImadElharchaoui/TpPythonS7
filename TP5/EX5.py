import json
students = [
    {"nom": "Imad", "age": 21, "note": 20},
    {"nom": "Nadi", "age": 12, "note": 15},
    {"nom": "hmdallah", "age": 3, "note": 7},
]

with open("TP5/etudiants.json", "w") as file:
    json.dump(students, file)

with open("TP5/etudiants.json", "r") as file:
    data = json.load(file)
    for student in data:
        print(f"Nom: {student['nom']}, Age: {student['age']}, Note: {student['note']}")
