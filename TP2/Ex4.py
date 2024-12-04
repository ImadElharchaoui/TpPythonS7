class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
    def se_presenter(self):
        print(f"je m'appelle {self.prenom} {self.nom} j'ai {self.age} annee")
    
class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        self.matricule = matricule
        super().__init__(nom, prenom, age)

P1 = Personne("harchaoui", "imad", 21)
E1 = Etudiant("harchaoui", "JOJO", 19, "D2312451")

P1.se_presenter()
E1.se_presenter()
        