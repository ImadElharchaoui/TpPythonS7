class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []
    def se_presenter(self):
        print(f"je m'appelle {self.prenom} {self.nom} j'ai {self.age} annee")
    def ajouter_ami(self, ami):
        if isinstance(ami, Personne):   
            self.amis.append(ami)
            ami.amis.append(self)
        else:
            print("ami ajouter n'est pas un personne")
    def afficher_amis(self):
        print("les amis de", self.prenom)
        for ami in self.amis:
            ami.se_presenter()
        print("-----------------------------")

P1 = Personne("harchaoui", "imad", 21)
P2 = Personne("ra9m2", "wa7ed", 1)
P3 = Personne("da2ira", "joj", 15)
P4 = Personne("motalat", "tata", 24)

P1.ajouter_ami(P2)
P1.ajouter_ami(P3)
P1.ajouter_ami(P4)

P1.afficher_amis()
P2.afficher_amis()

