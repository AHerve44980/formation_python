

class Animal:

    def __init__(self,nom):
        self._nom = nom         #protected
        self.__genetic = "ACG"  #private

    def emet_son(self):
        print("???")

    def __str__(self):
        return self.__class__.__name__ + " " + self._nom.upper()

a1 = Animal("coco")
a2 = Animal("lulu")

class Elephant(Animal):

    def __init__(self, nom, couleur):
        super().__init__(nom)  #fait comme m
        self.couleur = couleur

    def emet_son(self):
        print(f"Je suis `{self._nom} et je barris")

class Serpent(Animal):
    def __init__(self, nom):
        super().__init__(nom)  #fait comme m

    def emet_son(self):
        print("Je fais SSSSsssss")

ani1 = Animal("gege")
ele2 = Elephant("jumbo","gris")
ele3 = Elephant("grandjumbo","blanc")
ser0 = Serpent("kaa")

for xyz in (ani1,ele2,ser0,ele3):
    xyz.emet_son()
    print(xyz)


print('-'*20)
print(isinstance(ele2, Elephant))
print(isinstance(ser0, Elephant))
print(isinstance(ani1, Serpent))
print(isinstance(ser0, Animal))
