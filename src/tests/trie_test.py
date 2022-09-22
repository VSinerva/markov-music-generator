import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        """Alustus testejä varten."""
        self.trie = Trie()

    def test_lisaa(self):
        self.assertFalse(self.trie.juuri.lapset)

        self.trie.lisaa("AB")

        self.assertTrue("A" in self.trie.juuri.lapset)
        self.assertFalse("B" in self.trie.juuri.lapset)
        self.assertEqual(0, self.trie.juuri.lapset["A"].laskuri)
        self.assertEqual(1, self.trie.juuri.lapset["A"].lapset["B"].laskuri)

        self.trie.lisaa("AB")

        self.assertEqual(2, self.trie.juuri.lapset["A"].lapset["B"].laskuri)

    def test_etsi_seuraavat(self):
        self.assertFalse(self.trie.etsi_seuraavat("AB"))
        self.trie.lisaa("ABC")
        self.trie.lisaa("ABC")
        self.assertEqual(self.trie.etsi_seuraavat("AB"), ([1], ["C"]))
        self.trie.lisaa("ABC")
        self.trie.lisaa("ABD")

        todennakoisyydet, merkit = self.trie.etsi_seuraavat("AB")
        #Tällä saadaan järjestetty lista merkkejä ja todennäköisyyksiä, joka helpottaa testaamista
        lista = sorted(zip(todennakoisyydet, merkit), reverse=True)
        self.assertEqual(lista, [(0.75, "C"), (0.25, "D")])

        todennakoisyydet, merkit = self.trie.etsi_seuraavat("AB")
