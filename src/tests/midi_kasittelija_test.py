import os
import unittest
from midi_kasittelija import LueMidi, KirjoitaMidi

class TestMidiKasittelija(unittest.TestCase):
    def test_molemmat(self):
        testi_polku = "src/tests/testiMidi.mid"
        if os.path.exists(testi_polku):
            os.remove(testi_polku)

        nuotit = [60, 62, 64]
        KirjoitaMidi(testi_polku, nuotit)
        luetut_nuotit = LueMidi(testi_polku)[0]
        self.assertEqual(nuotit, luetut_nuotit)
