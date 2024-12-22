class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def prix_avec_remise(self, remise):
        if self.__prix > 100:
            return self.__prix * (1 - remise / 100)
        return self.__prix

p1 = Produit("pc", 150)
print(p1.prix_avec_remise(10)) 
