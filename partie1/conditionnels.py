nom = "frederic"

if nom.startswith("c"):
    print("commence par c effectivement")
    #si c 'est vrai

if nom[0] == "c":
    print("commence par c effectivement")

x = 2
condition = x**0.5 > 0
if condition:
    #si c'est vrai
    print("Une racine carré est > 2")
else:
    #si c'est faux
    print("Un carré est <= 2")

sequence = {1,2,4,8,16}
if 4 in sequence:
    print('4')

dico = { "one" : 1, "two" : 2, "four" : 4,2: "two" }
if "two" in dico: #équivalent à dico.keys()
    print('2 trouvé')
else:
    print("pas trouvé two")

dico = { "one" : 1, "two" : 2, "four" : 4,2: "two" }
if "two" in dico.values():
    print('2 trouvé')
else:
    print("pas trouvé two")

# BOUCLES

employees = {"aurelien","caroline","benoit","jean-christophe"}
foot = {"caroline","benoit","vivian"}

for item in employees:
    print(item)

for key in dico:
    print(key, dico[key])

print(dico.items())

for t in dico.items():
    print(t[0], ">>>>", t[1])

for key,val in dico.items():
    print(key, ">>>>", val)