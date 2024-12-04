class Animal:
    def __init__(self):
        pass
    
    def faire_du_bruit(self):
        print("Animal fait des Unkowned Bruit")

class Chien(Animal):
    def __init__(self):
        super().__init__()
    def faire_du_bruit(self):
        print("Woof!")

class Chat(Animal):
    def __init__(self):
        super().__init__()
    def faire_du_bruit(self):
        print("Meow!")


A1 = Animal()
Chein1 = Chien()
Chat1 = Chat()

A1.faire_du_bruit()
Chein1.faire_du_bruit()
Chat1.faire_du_bruit()
