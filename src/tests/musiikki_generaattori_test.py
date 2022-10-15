import os
import unittest
from musiikki_generaattori import musiikki_generaattori
from midi_kasittelija import lue_midi, kirjoita_midi 

class TestMusiikkiGeneraattori(unittest.TestCase):
    def test_kokonaisuus(self):
        testi_polku = "src/tests/testiMidi.mid"
        if os.path.exists(testi_polku):
            os.remove(testi_polku)

        nuotit = [60, 62, 64, 66, 68, 60, 62, None]
        kirjoita_midi(testi_polku, nuotit)

        musiikki_generaattori.lue_opetusdata("src/tests/testiMidi.*")

        musiikki_generaattori.valmistele_ketju("C4")
        musiikki_generaattori.generoi_nuotteja(4)
        musiikki_generaattori.kirjoita_midi(testi_polku)
        generoidut_nuotit = lue_midi(testi_polku)[0]
        self.assertEqual(generoidut_nuotit, nuotit[:4])

        musiikki_generaattori.valmistele_ketju("C4", aste=2)
        musiikki_generaattori.generoi_nuotteja(4)
        musiikki_generaattori.kirjoita_midi(testi_polku)
        generoidut_nuotit = lue_midi(testi_polku)[0]
        self.assertEqual(generoidut_nuotit, nuotit[:4])

        musiikki_generaattori.valmistele_ketju("C5")
        self.assertEqual(musiikki_generaattori.generoi_nuotteja(10), 1)
