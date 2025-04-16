from partie2.ateliers import miscellaneous
from partie2.ateliers.miscellaneous import affichage


class Livre:

        def __init__(self, titre, chemin_contenu, stops = () ):
            self.__titre = titre
            self.__fichier = chemin_contenu
            self.__lignes = None
            self.__stats = None
            self.__stop_words = stops

        def titre(self):
            return self.__titre

        def lire(self):
            print("Je vais lire ce livre : " + self.__titre)
            self.__lignes = miscellaneous.lecture_fichier(self.__fichier)

        """
        def calcul_stats(self):
            if self.lignes:
                self.stats = miscellaneous.calcul_occurences(self.lignes, self.stop_words)
        """
        def calcul_stats(self):
            if self.__lignes is None:
                self.lire()
            self.__stats = miscellaneous.calcul_occurences(self.__lignes, self.__stop_words)

        def palmares(self):
            if self.__stats is None:
                self.calcul_stats()

            affichage(self.__stats)

        def occurence(self, mot):
            if self.__stats is None:
                self.calcul_stats()

            if mot not in self.__stats:
                return 0
            return self.__stats[mot]

        def ratio(self, mot):
            if self.__stats is None:
                self.calcul_stats()

            # le rapport mot par aux autres mots
            return self.occurence(mot) / sum(x[1] for x in self.__stats.items())





