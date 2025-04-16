#Calcul de base
"""
celsius <-> farenheit
Transformer
"""
#celcius = input("Donne-moi une température en °C :")

celcius = "10.00"
celcius = float(celcius) #typage explicite

farhenheit = (celcius * 9 / 5) + 32
re_celcius = (farhenheit - 32) * 5/9

print(farhenheit, celcius, re_celcius, sep=" / ") #3 sur la même ligne

# Ouvrir un fichier (EXPLICATION A VENIR)
f = open("liste_de_mots.txt",encoding="utf-8")
phrase = f.readline()
phrases = f.readlines()
f.close()

print(phrases)

#MANIPULATION DE STR
# Du point de vue str
est_equipe = phrase.startswith("Equipe") #variable.fonction (convertit, teste, affiche)
print(est_equipe)

#SCLICING
print(phrase[0])
print(phrase[5])
print(phrase[0:5]) #On s'arrête avant la 6ème valeur (limite, pas taille)
print(phrase[5:])

#De 3 à 13, un caractère sur 2
print(phrase[3:13:2])

print(phrase[:13:2])
print(phrase[3::2])
print(phrase[::2]) #Les carac en position 0,2,4 PAIR
print(phrase[1::2]) #Les carac en postion 1,3,5 IMPAIR

# chaine[start:end:step]

print(phrase[-2]) #-1 = \n
print(phrase[-5:-2])
print(phrase[:-12])
print(phrase[-8:-2:2])

print(phrase[::-1])

nom_part = "PITOU"
print(nom_part[::-1])
print("PITOU"[::-1])

autre_nom= "THISISANAME"[::-1]
print(list(autre_nom))

#EXPLOITE LE COTE SEQUENTIEL
nbres = [1,2,3,4,5,6]
print(nbres)
print(nbres[::-1],nbres[-1],sep='#')





