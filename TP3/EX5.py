class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.equipes = []

    def ajouter_employe(self, employe):
        self.equipes.append(employe)
    
    def afficher_equipes(self):
        for emp in self.equipes:
            print(f"{emp.nom} {emp.prenom}")

manager = Manager("imad", "Nadi", 5000)
employe1 = Employe("neymar", "Junior", 3000)
manager.ajouter_employe(employe1)
manager.afficher_equipes()  
