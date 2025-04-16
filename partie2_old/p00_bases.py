from datetime import datetime

from partie1.specialites import aujourdhui


class Personne:
    # proprietes / attributs / fields
    #nom, prenom, date_naissance, metier
    # __ini__ est une fonction

    def __init__(self, nom, prenom, date_naissance, metier):
        self.nom = nom
        self.prenom = prenom
        self.naissance = datetime.fromisoformat(date_naissance)
        self.job = metier

    def __str__(self):
    #def identite(self):
        return f"{self.prenom} {self.nom} {self.job} {self.age()}"

    def age(self):
        aujourdhui = datetime.today()
        return aujourdhui.year - self.naissance.year

    def change_metier(self, nouveau_metier):
        if nouveau_metier is None:
            print("Metier vide !!!")
        else:
            self.job = nouveau_metier

# ---
vivian = Personne("wong", "vivian", "2001-01-15","CEO Proton")
caroline = Personne("taton","caroline","2005-02-15","jardinier")
ronaldo = Personne("drumond","ronaldo","2005-01-31","écrivain")
gaetan = Personne("dolige","gaetan","2003-01-02","ingénieur")

print(ronaldo.job)
print(vivian.job)
print(caroline.job)
print("-"*20)

# afficher les identités de tous
people = (gaetan, ronaldo, vivian, caroline)
for p in people:
    #print(p.identite())
    print(p)

print("-" * 20)

# change pour tous
for p in people:
    p.change_metier("menuisier/ebeniste")
    #print(p.identite())
    print(p)


# incertitude
vivian.naissance = None
vivian.change_metier(None)

# modèle de la variable naissance
print(type(ronaldo.naissance))
print(type(vivian.naissance))
print(vivian.job)

    # identite()

    # age()

    # change_metier()




# objet