from trie import Trie
from collections import deque
from random import choices

class MarkovKetju:
    def __init__(self, aste=1, trie=Trie()):
        self._trie = trie
        self._aste = aste
        self._menneet_tilat = deque()

    def kasittele_opetusdata(self, opetusdata: list):
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
        if len(alkuosa) < self._aste:
            raise ValueError("Liian lyhyt alkuosa!")
        self._menneet_tilat = deque([alkuosa[i] for i in range(0, self._aste)])

    def seuraava(self):
        if len(self._menneet_tilat) < self._aste:
            raise ValueError("Markovin ketjulle ei ole asetettu sopivaa alkuosaa!")

        todennakoisyydet, merkit = self._trie.etsi_seuraavat(self._menneet_tilat)

        if todennakoisyydet and merkit:
            seuraava = choices(merkit, weights=todennakoisyydet)[0]

            self._menneet_tilat.popleft()
            self._menneet_tilat.append(seuraava)

            return seuraava

        return None
