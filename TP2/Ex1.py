class Chien:
    def __init__(self, nom, race, age):
        self.nom = nom
        self.race = race
        self.age = age
    def aboyer(self):
        print("woof!")
    
chien1 = Chien("fahd", "3za", 12)
chien1.aboyer()