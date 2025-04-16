from partie1.ateliers.atelier2_compteur import affichage
from partie2.ateliers import misc2

class Livre:
    def __init__(self, titre, chemin_contenu, stops=()):
        self.__titre = titre
        self.fichier = chemin_contenu
        self.__lignes = None
        self.__stats = None
        self.__stop_words = stops

    def titre(self):
        return self.__titre

    def lire(self):
        print("Je vais lire ce livre : " + self.__titre)
        self.__lignes = misc2.lecture_fichier(self.fichier)

    def calcul_stats(self):
        self.__stats = misc2.calcul_occurences(self.__lignes, self.__stop_words)

    def palmares(self):
        affichage(self.__stats)

    def occurence(self, mot):
        if self.__stats is None:
            raise ValueError("Les statistiques n'ont pas été calculées.")
        if mot not in self.__stats:
            return 0
        return self.__stats[mot]

    def ratio(self, mot):
        if self.__stats is None:
            raise ValueError("Les statistiques n'ont pas été calculées.")
        return self.occurence(mot) / sum(x[1] for x in self.__stats.items())
