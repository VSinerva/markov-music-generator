"""Omaa trie-tietorakennetta käyttävä n-asteen Markovin ketju.
Käyttö:
from markov_ketu import MarkovKetju
"""
from collections import deque
from random import choices
from trie import Trie

class MarkovKetju:
    """n-asteen Markovin ketju"""
    def __init__(self, aste=1, trie=Trie()):
        """Aste voi olla mikä tahansa kokonaisluku n > 0. Uuden trien luomisen sijaan
        ketjulle voi syöttää valmiin trien.
        """
        if aste < 1:
            raise ValueError("Aste ei voi olla < 1!")

        self._trie = trie
        self._aste = aste
        self.menneet_tilat = deque()

    def kasittele_opetusdata(self, opetusdata: list):
        """Lukee opetusdata Markovin ketjun omaan trie-rakenteeseen.
        Opetusdatan muoto on lista, jossa mikä tahansa määrä iteroitavia näytteitä. Esim:
            ["ABC", "ABB", "AAAAAA"]
        """
        self._trie = Trie()

        for jono in opetusdata:
            if len(jono) > self._aste:
                alkio = deque(jono[0:self._aste+1])
                self._trie.lisaa(alkio)

                for i in range(self._aste+1, len(jono)):
                    alkio.popleft()
                    alkio.append(jono[i])
                    self._trie.lisaa(alkio)

    def aseta_alkuosa(self, alkuosa):
        """Asettaa alkuosan, jonka perusteella Markovin ketju luo seuraavan merkin.
        Alkuosan pituus on sama kuin ketjun aste, liian pitkästä alkuosasta jätetään
        loppu pois.
        """
        if len(alkuosa) < self._aste:
            raise ValueError("Liian lyhyt alkuosa!")
        self.menneet_tilat = deque([alkuosa[i] for i in range(0, self._aste)])

    def seuraava(self):
        """Antaa seuraavan merkin muilla funktioilla annettujen opetusdata ja alkuosan
        perusteella. Päivittää alkuosan automaattisesti seuraavaa askelta varten
        """
        if len(self.menneet_tilat) < self._aste:
            raise ValueError("Markovin ketjulle ei ole asetettu sopivaa alkuosaa!")

        todennakoisyydet, merkit = self._trie.etsi_seuraavat(self.menneet_tilat)

        if todennakoisyydet and merkit:
            #Valitsee merkeistä yhden, valinta painotetaan triessä olevien todennäköisyyksien avulla
            seuraava = choices(merkit, weights=todennakoisyydet)[0]

            #Päivittää alkuosan seuraavaa iteraatiota varten
            self.menneet_tilat.popleft()
            self.menneet_tilat.append(seuraava)

            return seuraava

        return None
