"""Mahdollistaa musiikin generoinnin Markovin ketjujen avulla.
from musiikki_generaattori import musiikki_generaattori
"""
from collections import deque
from glob import glob
from markov_ketju import MarkovKetju
from midi_kasittelija import lue_midi, kirjoita_midi
from trie import Trie

class MusiikkiGeneraattori:
    """Yhden instanssin luokka musiikin generoimiseen."""
    def __init__(self):
        self._ketju = None
        self._nuotit = []
        self._opetusdata = []

        self._nuotti_midiksi = {
                "C":0,
                "C#":1,
                "DB":1,
                "D":2,
                "D#":3,
                "EB":3,
                "E":4,
                "F":5,
                "F#":6,
                "GB":6,
                "G":7,
                "G#":8,
                "AB":8,
                "A":9,
                "A#":10,
                "BB":10,
                "B":11}

    def lue_opetusdata(self, polku):
        """Lukee nuotit annetun polun MIDI-tiedostoista.
        Useamman tiedoston lukeminen *-merkillä esim 'kansio/*.mid'
        """
        tiedostot = glob(polku)
        self._opetusdata = []

        for tiedosto in tiedostot:
            try:
                for jono in lue_midi(tiedosto):
                    self._opetusdata.append(jono)
            # Kaikki virheet halutaan ohittaa
            except: # pylint: disable=bare-except
                continue

    def valmistele_ketju(self, alkuosa, aste=1):
        """Luo ja valmistelee halutun asteisen Markovin ketjun annetulla alkuosalla"""
        alkuosa = self._nuotit_midiksi(alkuosa)

        if len(alkuosa) < aste:
            trie = Trie()

            # Rakentaa poikkeuksellisesti Trien, jossa on kaikki ENINTÄÄN 'aste' mittaiset alkiot,
            # jotka löytyvät opetusdatasta.
            for jono in self._opetusdata:
                if len(jono) > aste:
                    alkio = deque()

                    for nuotti in jono:
                        if len(alkio) > aste:
                            alkio.popleft()
                        alkio.append(nuotti)
                        for i in range(-len(alkio), 0):
                            trie.lisaa([alkio[x] for x in range(i, 0)])

            # Täydentää alkuosan riittävän pitkäksi käyttämällä asteittain pidempiä Markovin ketjuja
            alkuosa = list(alkuosa)
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

    def generoi_nuotteja(self, maara):
        """Generoi halutun määrän nuotteja aiemmin alustetulla Markovin ketjulla"""
        self._nuotit = list(self._ketju.menneet_tilat)
        nuotteja = maara - len(self._nuotit)
        for _ in range(nuotteja):
            # Tunnistaa jos edellinen Markovin ketjun iteraatio palautti None
            if not self._nuotit[-1]:
                break
            self._nuotit.append(self._ketju.seuraava())

        return len(self._nuotit)

    def kirjoita_midi(self, tiedostopolku, tempo=120):
        """Kirjoittaa nuotit MIDI-tiedostoon halutulla tempolla"""
        kirjoita_midi(tiedostopolku, self._nuotit, tempo)

    def _nuotit_midiksi(self, nuotit: str):
        """Muuttaa perinteiset nuottimerkinnät kuten C#4 MIDI-arvoiksi"""
        nuotit = nuotit.split("|")
        midi = []
        for nuotti in nuotit:
            arvo = (int(nuotti[-1])+1) * 12
            arvo += self._nuotti_midiksi[nuotti[:-1].upper()]
            midi.append(arvo)
        return midi

musiikki_generaattori = MusiikkiGeneraattori()
