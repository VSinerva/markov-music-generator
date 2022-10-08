import os
import unittest
from midi_kasittelija import lue_midi, kirjoita_midi 

class TestMidiKasittelija(unittest.TestCase):
    def test_molemmat(self):
        testi_polku = "src/tests/testiMidi.mid"
        if os.path.exists(testi_polku):
            os.remove(testi_polku)

        nuotit = [60, 62, 64, 66, 68, None]
        kirjoita_midi(testi_polku, nuotit, tempo=120, rytmi="1/4|1")
        luetut_nuotit = lue_midi(testi_polku)[0]
        self.assertEqual(nuotit[:-1], luetut_nuotit)

        nuotit = [None]
        kirjoita_midi(testi_polku, nuotit)
        luetut_nuotit = lue_midi(testi_polku)
        self.assertEqual([], luetut_nuotit)

    def test_molli_ja_transponointi(self):
        testi_polku = "src/tests/testiMidi2.mid"
        nuotit = [60, 62, 64, 60, 62, 64]
        luetut_nuotit = lue_midi(testi_polku)[0]
        self.assertEqual(nuotit, luetut_nuotit)
