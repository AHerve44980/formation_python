from partie2.modeles.livre import Livre

# Donnees plus clairement identifiées
mcristo = Livre("Monte Cristo","../data/monte_cristo.txt")
vingtmille = Livre("20 000 Lieues sous les Mers","../data/20_000_leagues.txt")

livres = {mcristo, vingtmille}

"""
for lv in livres:
    for m in ("20-000-lieues", "nemo"):
        print(f"{lv.titre()} => {lv.ratio(m):.10f}")
"""

for lv in livres:
    lv.lire()
    lv.calcul_stats()
    print(lv.titre(), lv.ratio("vengeance"))
    print(lv.titre(), lv.ratio("nemo"))



