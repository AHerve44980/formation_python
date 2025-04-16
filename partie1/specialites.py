# for
import math
import datetime

#PAS PYTHONIQUE
nombres = [1.0,2.0,5.0,8.5]
racines = []
for n in nombres:
    # racine carrée de
    racines.append( math.sqrt(n))
print(racines)


# liste en compréhension
racines = [math.sqrt(n) for n in nombres]
print(racines)

# set (pas dans l'ordre)
setracines = {math.sqrt(n) for n in nombres}
print(setracines)

# dictionnaire en compréhension
dicoracines = {n:math.sqrt(n) for n in nombres}
print(dicoracines)

# test en ligne / ternaires
a_tester = 8
a = 5
if a_tester > 5:
    a = 10

a = 10 if a_tester > 5 else 5 # ternaire (vrai, test, faux)


# CONTEXT MANAGER (ex. fichiers)
"""
with open("f.txt") as f:
    f.read()
    """


# LAMBDA
# lambda
def maxi(list_valeurs):
    return max(list_valeurs)

# en raccourci
maxil = lambda lv : max(lv)

# Une fonction est une variable qui pointe sur du code
maxil([1,2,3])
print(maxil([1,2,3]))

def queljoureston():
    return datetime.date.today()

queljour = lambda : datetime.date.today()
#print(queljour())
aujourdhui = queljour()

td = datetime.timedelta(days=2, hours=5, minutes=30)

avant = aujourdhui - td
print(avant)
print(avant.weekday())

# GENERATEUR
# range
liste_valeurs = [1,2,3,4,5,None,100000]

for lv in range(100000):
    # print(lv) <- economiser de la memoire
    pass
#exemple : read, readline de file.read()

#
val1 = 5
val2 = math.sqrt(2)
val3 = "fin"
message = "v={} racine={} mot:{}".format(val1,val2,val3)
print(message)

message = "v={:03d} racine={:1.3f} mot:{:>30}".format(val1,val2,val3)
print(message)

# version raccourcie
message = f"v={val1:03d} racine={val2:1.3f} mot:{val3:>30}"
print(message)


#