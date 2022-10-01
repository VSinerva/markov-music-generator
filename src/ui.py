"""Musiikki generaattorin tekstipohjainen käyttöliittymä
from ui import UI"""
from os import system, name
from re import search
from sys import exit as sys_exit
from musiikki_generaattori import musiikki_generaattori

class UI: # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Tekstipohjainen käyttöliittymä. Käynnistyy automaattisesti, kun olio luodaan"""
    def __init__(self):
        self._opetusdata_polku = "opetusdata/*.mid"
        self._tulos_polku = "savelma.mid"
        self._aste = 1
        self._alku = "C4"
        self._nuottien_maara = 100
        self._tempo = 120

        self._toiminnot = {
                "A": ("(A)pu", self._tulosta_apu, 0,
                    "Tulosta apu"),
                "O": ("(O)petusdata [polku]", self._aseta_opetusdata, 1,
                    "Valitse opetusdata"),
                "P": ("(P)olku [polku]", self._aseta_tulos_polku, 1,
                    "Valitse valmiin sävelmän polku"),
                "K": ("(K)etjun aste", self._aseta_aste, 1,
                    "Aseta Markovin ketjun aste valittuun kokonaislukuun"),
                "L": ("a(L)kuosa [merkkijono]", self._aseta_alkuosa, 1,
                    "Aseta alkuosa. Esim. 'C4|D#5|Gb3'"),
                "N": ("(N)uotteja [luku]", self._aseta_nuottien_maara, 1,
                    "Aseta sävelmän nuottien määrä valittuun kokonaislukuun"),
                "T": ("(T)empo [luku]", self._aseta_tempo, 1,
                    "Aseta tempo valittuun kokonaislukuun"),
                "G": ("(G)eneroi sävelmä", self._generoi_savelma, 0,
                    "Generoi sävelmä valituilla asetuksilla"),
                "S": ("(S)ulje", self._sulje, 0,
                    "Sulje ohjelma")
                }

        self._virheet = []


        self._tyhjenna()
        self._suorita()

    def _suorita(self):
        while True:
            self._tulosta_virheet()

            self._tulosta_arvot()

            komento = input("\nKomento ('A' tulostaaksesi apu): ")

            self._tyhjenna()

            if komento:
                if komento[0].upper() in self._toiminnot:
                    # Virheiden välttämiseksi sulkeminen käsitellään ennen muita
                    if komento[0].upper() == "S":
                        self._sulje()

                    _, funktio, parametrien_maara, _ = self._toiminnot[komento[0].upper()]
                    komento = komento.split(" ")

                    try:
                        parametrit = []
                        for i in range(1, 1+parametrien_maara):
                            parametrit.append(komento[i])
                        funktio(parametrit)
                    # Kaikki virheet halutaan ohittaa
                    except: # pylint: disable=bare-except
                        self._virheet.append("KOMENNON MUOTO VÄÄRÄ!")

    def _tyhjenna(self):
        # windows
        if name == "nt":
            _ = system("cls")

        # mac ja linux
        else:
            _ = system("clear")

    def _tulosta_virheet(self):
        if self._virheet:
            while self._virheet:
                print(self._virheet.pop())
            print()
        self._virheet = []

    def _tulosta_arvot(self):
        print(f"Opetusdata: '{self._opetusdata_polku}'")
        print(f"Generoidun sävelmän polku: '{self._tulos_polku}'")
        print()
        print(f"Markovin ketjun aste: {self._aste}")
        print(f"Sävelmän pituus nuotteina: {self._nuottien_maara}")
        print(f"Tempo: {self._tempo}")
        print(f"Alkuosa: '{self._alku}'")

    def _tulosta_apu(self, _):
        print("OHJEET")
        print("----------------\n")
        for _, toiminto in self._toiminnot.items():
            nimi, _, _, kuvaus = toiminto
            print(f"{nimi}: {kuvaus}")
        print("\n----------------")

    def _aseta_opetusdata(self, polku):
        self._opetusdata_polku = polku[0]

    def _aseta_tulos_polku(self, polku):
        self._tulos_polku = polku[0]

    def _aseta_aste(self, aste):
        try:
            self._aste = int(aste[0])
        except ValueError:
            self._virheet.append("ANNETTU ASTE EI MUUTETTAVISSA KOKONAISLUVUKSI!")

    def _aseta_alkuosa(self, alkuosa):
        alkuosa = alkuosa[0]
        if search(r"^([CcDdEeFfGgAaBb][#b]?[0-8]\|)*[CcDdEeFfGgAaBb][#b]?[0-8]$", alkuosa):
            self._alku = alkuosa
        else:
            self._virheet.append("ANNETTU ALKUOSA EI KELPAA!")

    def _aseta_nuottien_maara(self, nuotteja):
        try:
            self._nuottien_maara = int(nuotteja[0])
        except ValueError:
            self._virheet.append("ANNETTU NUOTTIEN MÄÄRÄ EI MUUTETTAVISSA KOKONAISLUVUKSI!")

    def _aseta_tempo(self, tempo):
        try:
            self._tempo = int(tempo[0])
        except ValueError:
            self._virheet.append("ANNETTU TEMPO EI MUUTETTAVISSA KOKONAISLUVUKSI!")

    def _generoi_savelma(self, _):
        musiikki_generaattori.lue_opetusdata(self._opetusdata_polku)
        musiikki_generaattori.valmistele_ketju(self._alku, self._aste)

        generoitu_maara = musiikki_generaattori.generoi_nuotteja(self._nuottien_maara)
        print(f"Generoitiin {generoitu_maara} nuottia!\n")
        musiikki_generaattori.kirjoita_midi(self._tulos_polku, self._tempo)

    def _sulje(self):
        sys_exit(0)
