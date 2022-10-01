from collections import deque
from glob import glob
from markov_ketju import MarkovKetju
from midi_kasittelija import lue_midi, kirjoita_midi 
from trie import Trie


class MusiikkiGeneraattori:
    def __init__(self):
        self._ketju = None
        self._nuotit = []
        self._opetusdata = []

        self._nuotti_midiksi = {
                "C":0,
                "C#":1,
                "Db":1,
                "D":2,
                "D#":3,
                "Eb":3,
                "E":4,
                "F":5,
                "F#":6,
                "Gb":6,
                "G":7,
                "G#":8,
                "Ab":8,
                "A":9,
                "A#":10,
                "Bb":10,
                "B":11}

    def lue_opetusdata(self, polku):
        tiedostot = glob(polku)
        self._opetusdata = []

        for tiedosto in tiedostot:
            try:
                for x in lue_midi(tiedosto):
                    self._opetusdata.append(x)
            except:
                continue

    def valmistele_ketju(self, alkuosa, aste=1):
        alkuosa = self._nuotit_midiksi(alkuosa)

        if len(alkuosa) < aste:
            trie = Trie()

            for jono in self._opetusdata:
                if len(jono) > aste:
                    alkio = deque()

                    for i in range(0, len(jono)):
                        if len(alkio) > aste:
                            alkio.popleft()
                        alkio.append(jono[i])
                        for j in range(-len(alkio), 0):
                            trie.lisaa([alkio[x] for x in range(j, 0)])

            alkuosa = [x for x in alkuosa]
            while len(alkuosa) < aste:
                self._ketju = MarkovKetju(len(alkuosa), trie)
                self._ketju.aseta_alkuosa(alkuosa)
                alkuosa += [self._ketju.seuraava()]

            self._ketju = MarkovKetju(aste, trie)
            self._ketju.aseta_alkuosa(alkuosa)

        else:
            self._ketju = MarkovKetju(aste)
            self._ketju.kasittele_opetusdata(self._opetusdata)
            self._ketju.aseta_alkuosa(alkuosa)

    def generoi_nuotteja(self, n):
        self._nuotit = list(self._ketju.menneet_tilat)
        nuotteja = n - len(self._nuotit)
        for i in range(nuotteja):
            # Tunnistaa jos edellinen Markovin ketjun iteraatio palautti None
            if not self._nuotit[-1]:
                break
            self._nuotit.append(self._ketju.seuraava())

        return len(self._nuotit)

    def kirjoita_midi(self, tiedostopolku, tempo=120):
        kirjoita_midi(tiedostopolku, self._nuotit, tempo)

    def _nuotit_midiksi(self, nuotit: str):
        nuotit = nuotit.split(" ")
        midi = []
        for nuotti in nuotit:
            arvo = (int(nuotti[-1])+1) * 12
            arvo += self._nuotti_midiksi[nuotti[:-1]]
            midi.append(arvo)
        return midi

musiikki_generaattori = MusiikkiGeneraattori()
