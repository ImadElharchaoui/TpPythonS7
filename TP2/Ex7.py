class Livre:
    def __init__(self, titre, auteur, annee_prod):
        self.titre = titre
        self.auteur = auteur
        self.annee_prod = annee_prod
    def afficher_livre(self):
        print(f"titre: {self.titre}, auteur: {self.auteur}, Annee: {self.annee_prod}")

class Biblio:
    def __init__(self, livres):
        self.livres= livres
    
    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        for livre in self.livres:
            livre.afficher_livre()

L1 = Livre("titre1", "imad", 2333)
L2 = Livre("tit2", "imad", 2333)
L3 = Livre("tttt", "imad", 2333)
L4 = Livre("ajouted", "imad", 2333)

bib1 = Biblio([L1, L2, L3])
bib1.afficher_livres()
print("----------------------------------------------")
bib1.ajouter_livre(L4)
bib1.afficher_livres()

