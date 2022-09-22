import unittest
from markov_ketju import MarkovKetju

class TestMarkovKetju(unittest.TestCase):
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
