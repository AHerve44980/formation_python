from partie2.modeles.livre import Livre

# Données plus clairement identifiées
mcristo = Livre("Monte Cristo", "../data/monte_cristo.txt")
vingtmille = Livre("20 000 Lieues", "../data/20_000_leagues.txt")

livres = [mcristo, vingtmille]

for lv in livres:
    lv.lire()
    lv.calcul_stats()
    print(lv.titre(), lv.ratio("monte-cristo"))
    print(lv.titre(), lv.ratio("nemo"))
