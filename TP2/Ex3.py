class CompteBancaire:
    def __init__(self, titulaire, sold):
        self.titulaire = titulaire
        self.sold = sold
    def deposer(self, montant):
        self.sold += montant
    def retirer(self, montant):
        if(self.sold < montant):
            print("sold ne pas suffisent pour retirer le montant")
        else:
            self.sold -= montant
            print("montant est retirer")
    def afficher_sold(self):
        print(f"sold est: {self.sold}")


compte1 = CompteBancaire("imad", 5000)
compte1.retirer(7000)
compte1.retirer(2000)
compte1.afficher_sold()
compte1.deposer(3000)
compte1.afficher_sold()
        