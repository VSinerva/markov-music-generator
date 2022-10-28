"""Markovin ketjuille tarkoitettu trie-tietorakenteen implementaatio.
Käyttö:
from trie import Trie
"""

class TrieSolmu: # pylint: disable=too-few-public-methods
    """Yksittäinen trie-tietorakenteen solmu. Sisältää Markovin ketjuille tarpeellisia tietoja."""
    def __init__(self):
        self.lapset = {}
        self.laskuri = 0
        self.todennakoisyys = 0.0

class Trie:
    """Trie-tietorakenne.
    Sisältää perusoperaatioiden lisäksi Markovin ketjuille tarpeellisia toimintoja.
    """

    def __init__(self):
        """Luo tyhjä trie-rakenne. Tyhjässä triessä on juurisolmu, jota ei vastaa mikään merkki."""
        self.juuri = TrieSolmu()
        self.todennakoisyydet_laskettu = True

    def lisaa(self, alkio):
        """Lisää alkio triehen.
        Luo tarvittavat solmut ja kasvata alkiota vastaavan solmun laskuria yhdellä.
        """

        #Kertoo, että todennäköisyydet tulee laskea uudestaan
        self.todennakoisyydet_laskettu = False

        solmu = self.juuri

        #Kulkee polun alkiota vastaavaan solmuun. Luo tarvittaessa solmuja
        for merkki in alkio:
            if merkki not in solmu.lapset:
                solmu.lapset[merkki] = TrieSolmu()
            solmu = solmu.lapset[merkki]

        solmu.laskuri += 1

    def laske_todennakoisyydet(self):
        """Laske solmujen lapsille todennäköisyys, kuinka todennäköisesti lasta vastaava merkki
        ilmenee kun muut merkit on jo nähty.
        """

        #Laskenta tehdään, vain jos se on tarpeellista.
        if self.todennakoisyydet_laskettu:
            return

        kasiteltavat_solmut = [self.juuri]

        #Solmut käsitellään syvyysjärjestyksessä, mutta tällä ei ole väliä
        while kasiteltavat_solmut:
            solmu = kasiteltavat_solmut.pop()
            summa = 0
            for _, lapsi in solmu.lapset.items():
                summa += lapsi.laskuri
                kasiteltavat_solmut.append(lapsi)
            if summa:
                for _, lapsi in solmu.lapset.items():
                    merkki.todennakoisyys = lapsi.laskuri / summa

        self.todennakoisyydet_laskettu = True

    def etsi_seuraavat(self, alkuosa):
        """Etsi alkuosaan sopivat viimeiset merkit ja niiden todennäköisyydet.
        Palauttaa tuplen listoja (tod., merkit).
        """

        #Funktion sisällä tarkistetaan onko laskenta tarpeellista
        self.laske_todennakoisyydet()

        solmu = self.juuri

        #Etsitään alkuosaa vastaava solmu
        for merkki in alkuosa:
            if merkki not in solmu.lapset:
                return (None, None)
            solmu = solmu.lapset[merkki]

        #Listaa kaikki alkuosan lapset
        todennakoisyydet = []
        merkit = []

        for merkki, lapsi in solmu.lapset.items():
            todennakoisyydet.append(lapsi.todennakoisyys)
            merkit.append(merkki)
        return (todennakoisyydet, merkit)
