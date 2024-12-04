class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"marque: {self.marque}, modele: {self.modele}, Annee: {self.annee}")
    
v1 = Voiture("bmw", "2009", 2010)
v2 = Voiture("jeep", "M", 2020)
v3 = Voiture("tesla", "X", 2025)
v1.afficher_info()
v2.afficher_info()
v3.afficher_info()