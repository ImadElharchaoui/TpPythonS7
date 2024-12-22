from EX4 import Produit

class Commande:
    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    def calculer_prix(self):
        return self.produit.prix_avec_remise(10) * self.quantite

class Panier:
    def __init__(self):
        self.commandes = []
    
    def ajouter_commande(self, commande):
        self.commandes.append(commande)
    
    def calculer_total(self):
        return sum(c.calculer_prix() for c in self.commandes)

produit = Produit("pc", 150)
commande = Commande(produit, 2)
panier = Panier()
panier.ajouter_commande(commande)
print(panier.calculer_total()) 
