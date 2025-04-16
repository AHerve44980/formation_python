#containers

# TOUT EST UN OBJET
# 4 CONTAINERS STANDARD
# LIST, TUPLE, SET, DICT

# list : une sequence ordonnee de valeurs, modifiable, sequence mutable
valeurs  = [1, None, "HP", 100.50, False]
v1= valeurs[1]
v2= valeurs[3]
v1,v2 = valeurs[1],valeurs[3] #unpacking
print(v1,v2, sep="-")

print(type(valeurs))
valeurs.append(6) #NOTATION POO

print(valeurs)

valeurs.pop(0)

print(valeurs.pop(0)) #LA LISTE EST MUTABLE
valeurs[-1] = 600
print(valeurs)

liste_vide = []
liste_vide = list()

#boucle : for

# tuple : une sequence ordonnee de valeurs, non mutable
tvaleurs  = (1, None, "HP", 100.50, False, "HP")

print(tvaleurs[2])

copy_tuple = tuple(valeurs)
copy_tuple = tuple([0,11,23,5,8,13,21,34])
print(copy_tuple)

# copy_tuple[0] = -1 #impossible


# SET (ensemble) : une sequence de valeurs, modifiable, sequence mutable
s_value = set(tvaleurs)
s2_value = {1,2,3,4,5} #SET à la diff de {} = dictionnaire
print(s_value)

employees = {"aurelien","caroline","benoit","jean-christophe"}
foot = {"caroline","benoit","vivian"}

club_foot = employees.intersection(foot)
print(club_foot)

edf = employees.difference(foot) #pas du foot dans cette societe
fde = foot.difference(employees) #qui ne sont pas employes par

print(edf)
print(fde)

#employees.pop() #Retire au hasard

# dictionnaire dict
# dict : un set de clés --> liste de valeurs

dico = dict()
dico =  {}
dico = { "one" : 1, "two" : 2, "four" : 4 }
dico["two"]
print('two vaut : ',dico["two"])

"""
lecture

list
tuple *
set **
dico ****

écriture

*
N/A
**
**

taille

**
**
***
*
"""

# déborde = erreur
taille = len(tvaleurs)
print(tvaleurs[taille-1])

#dico["three"]