class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    def calc_surface(self):
        return self.largeur * self.hauteur
    def calc_perimetre(self):
        return ( self.largeur + self.hauteur) * 2


R1 = Rectangle(10, 20)
print(f"surface: {R1.calc_surface()}, perimetre: {R1.calc_perimetre()}")
    

        