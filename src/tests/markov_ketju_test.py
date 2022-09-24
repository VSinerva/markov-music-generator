import unittest
from markov_ketju import MarkovKetju

class TestMarkovKetju(unittest.TestCase):

    def test_0_aste(self):
        self.assertRaises(ValueError, MarkovKetju, 0)

    def test_seuraava_1_aste(self):
        ketju = MarkovKetju(1)
        opetusdata = ["ABCDEA"]
        ketju.kasittele_opetusdata(opetusdata)
        ketju.aseta_alkuosa("E")

        self.assertEqual("A", ketju.seuraava())
        self.assertEqual("B", ketju.seuraava())
        self.assertEqual("C", ketju.seuraava())
        self.assertEqual("D", ketju.seuraava())
        self.assertEqual("E", ketju.seuraava())
        self.assertEqual("A", ketju.seuraava())

        ketju.aseta_alkuosa("F")
        self.assertFalse(ketju.seuraava())
 
    def test_seuraava_2_aste(self):
        ketju = MarkovKetju(2)
        opetusdata = ["ABCDEAB", "F"]
        ketju.kasittele_opetusdata(opetusdata)
        ketju.aseta_alkuosa("DE")

        self.assertEqual("A", ketju.seuraava())
        self.assertEqual("B", ketju.seuraava())
        self.assertEqual("C", ketju.seuraava())
        self.assertEqual("D", ketju.seuraava())
        self.assertEqual("E", ketju.seuraava())
        self.assertEqual("A", ketju.seuraava())

        self.assertRaises(ValueError, ketju.aseta_alkuosa, "F")
        ketju.aseta_alkuosa("EF")
        self.assertFalse(ketju.seuraava())

    def test_seuraava_todennakoisyys(self):
        """Testaa, että Markovin ketjun antamat merkit ilmenevät likimain oikeilla yleisyyksillä"""
        ketju = MarkovKetju(1)
        opetusdata = ["AA", "AB", "AB", "AC", "AC", "AC"]
        ketju.kasittele_opetusdata(opetusdata)

        """yhteensä ja marginaali määrittävät testin tarkkuuden ja toisaalta virheellisen hylkäämisen
        todennäköisyyden. 3000 iteraatiota ja 5% marginaali tarkoittaa, että todellinen määrä saa
        poiketa odotetusta enintään 3000*0,05 = 150, joka on mielestäni riittävän suuri tarkkuus.
        Todennäköisyys, että testi ei mene läpi, kun Markovin ketju toimii oikein, on luokkaa 10^-8.
        """
        yhteensa = 3000
        marginaali = 0.05

        a_maara = 0
        b_maara = 0
        c_maara = 0

        for i in range(yhteensa):
            ketju.aseta_alkuosa("A")
            merkki = ketju.seuraava()
            if merkki == "A":
                a_maara += 1
            elif merkki == "B":
                b_maara += 1
            elif merkki == "C":
                c_maara += 1

        a_osuus = a_maara / yhteensa # Pitäisi olla noin 1/6
        b_osuus = b_maara / yhteensa # Pitäisi olla noin 2/6
        c_osuus = c_maara / yhteensa # Pitäisi olla noin 3/6

        self.assertAlmostEqual(a_osuus, 1/6, delta=marginaali)
        self.assertAlmostEqual(b_osuus, 2/6, delta=marginaali)
        self.assertAlmostEqual(c_osuus, 3/6, delta=marginaali)
