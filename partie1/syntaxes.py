file_path = "C:/Windows/System32/f.txt" # chaine de caracteres
print( type(file_path))

#int
taille = 5400
print(type(taille))

# bool
prix_produit = 85.10

est_actif = True
est_disponible = False
print(type(est_actif))

# print(type(cpx))

cpx = 3j + 5
print(type)

#du type découle les possibilités d'utilisation

# .....
# perturbant - change le type de la variable cpx
# cpx = "Complex chaine"
print(type(cpx))

taux_tva = 20.0
prix_ht = 200

#Conversion :
message= "Prix TTC : "

prix_ttc = prix_ht * (1 + taux_tva/100) #CAST IMPLICITE (TRANSTYPAGE --> La donnée a choisi son type : qui peut le plus peut le moins)

prix_ttc = int(prix_ttc) #CAST EXPLICITE

print(prix_ttc, type(prix_ttc))

resultat = message + str(prix_ttc)
print(resultat)

texte = '19.5'
print(float(texte) / 100) # pas int car parse

print('Valeur' + str(taux_tva)) #operateur + --> opérateur contextuel

print('Valeur' * 10) #repete 10x la valeur

#Rien n'oblige à mettre une chaine de caracteres  --> indication donnee sur ce qui est souhaite
texte:str = "ronaldo drumond"

#Notation POO
texte.capitalize

print(texte.upper())