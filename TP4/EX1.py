class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Véhicule: {self.marque} {self.modele}, Année: {self.annee}")


class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur

    def afficher_moteur(self):
        print(f"Moteur: {self.puissance} chevaux, Type: {self.type_moteur}")



class Voiture(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, nombre_de_places):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.nombre_de_places = nombre_de_places

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Nombre de places: {self.nombre_de_places}")



class Moto(Vehicule, Moteur):
    def __init__(self, marque, modele, annee, puissance, type_moteur, type_moto):
        Vehicule.__init__(self, marque, modele, annee)
        Moteur.__init__(self, puissance, type_moteur)
        self.type_moto = type_moto

    def afficher_info(self):
        super().afficher_info()
        self.afficher_moteur()
        print(f"Type de moto: {self.type_moto}")



voiture1 = Voiture("dacia", "voiture1", 2025, 150, "Essence", 5)
voiture2 = Voiture("kongo", "voiture2", 2000, 115, "Essence", 2)
moto1 = Moto("C90", "Motor1", 2025, 75, "Essence", "Sport")


print("\n----------------------------------")

voiture1.afficher_info()
print("\n----------------------------------")

voiture2.afficher_info()
print("\n----------------------------------")

moto1.afficher_info()
