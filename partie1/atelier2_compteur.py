# Compter les occurrences de chaque mot
# Les mots d'une ligne sont séparés par des espaces
# Remplir la structure au fur et à mesure
# Une fois tout rempli, on affiche le résultat

from string import punctuation

# Définition des fonctions
def clean_line(phrase):
    punctuation_to_remove = punctuation.replace("-", "")
    phrase = phrase.lower()

    for c in punctuation_to_remove:
        phrase = phrase.replace(c, "")

    return phrase

def lecture_fichier(file_path):
    with open(file_path, encoding="utf-8") as fichier:
        lines = fichier.read().splitlines()  # Mieux que fichier.readlines() : fait disparaître le retour à la ligne

    # Convertir en minuscules et nettoyer les lignes
    lines = [clean_line(line) for line in lines]

    return lines

def charger_stop_words(file_path):
    with open(file_path, encoding="utf-8") as fichier:
        stop_words = set(fichier.read().splitlines())
    return stop_words

# Transformation (calcul, modifier les données)
def calcul_occurences(lines, stop_words=set()):
    occurences = {}

    for line in lines:
        words = line.split()
        for word in words:
            if word and word not in stop_words:  # Ignorer les mots vides et les stop words
            # ternaire
                occurences[word] = occurences[word] + 1 if word in occurences else 1
            """
                if word in occurences:
                    occurences[word] += 1
                else:
                    occurences[word] = 1
            """

    return occurences

def selection(tu):
    return tu[1]

def affichage(occurences, limite=-1):
    # Construire une liste triée à partir des occurrences
    sorted_list = list(occurences.items())
    sorted_list.sort(key=selection, reverse=True)  # Tri par ordre décroissant des occurrences

    # Affichage des résultats
    for word, occurence in sorted_list[:limite]:
        print(f"{word} : {occurence}")

    # Exemple d'affichage spécifique
    if "nemo" in occurences:
        print("nemo", occurences["nemo"])

if __name__ == "__main__":
    # Charger les stop words à partir du fichier
    stop_words = charger_stop_words("../data/stop_words.txt")

    # Appel des fonctions
    phrases = lecture_fichier("../data/20_000_leagues.txt")
    occs = calcul_occurences(phrases, stop_words)
    affichage(occs, 10)

# Un programme qui marche est le minimum du minimum
