class Personne:
    def __init__(self, nom, prenom, age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def getNom(self):
        return self.__nom
    
    def setNom(self, nom):
        if nom.isalpha():
            self.__nom = nom
    
    def getAge(self):
        return self.__age

    def setAge(self, age):
        if age > 0:
            self.__age = age

p1 = Personne("Imad", "Nadi", 30)
print(p1.getNom()) 
p1.setAge(35)
print(p1.getAge())
