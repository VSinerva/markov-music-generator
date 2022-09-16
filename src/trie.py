class TrieSolmu:
    def __init__(self):
        self.lapset = {}
        self.laskuri = 0
        self.todennakoisyys = 0.0

class Trie:
    def __init__(self):
        self.juuri = TrieSolmu()
        self.todennakoisyydet_laskettu = True

    def lisaa(self, alkio):
        self.todennakoisyydet_laskettu = False

        solmu = self.juuri

        for x in alkio:
            if x not in solmu.lapset:
                solmu.lapset[x] = TrieSolmu()
            solmu = solmu.lapset[x]
        solmu.laskuri += 1

    def laske_todennakoisyydet(self):
        if self.todennakoisyydet_laskettu:
            return

        kasiteltavat_solmut = [self.juuri]

        while kasiteltavat_solmut:
            solmu = kasiteltavat_solmut.pop()
            summa = 0
            for _, x in solmu.lapset.items():
                summa += x.laskuri
                kasiteltavat_solmut.append(x)
            if summa:
                for _, x in solmu.lapset.items():
                    x.todennakoisyys = x.laskuri / summa

        self.todennakoisyydet_laskettu = True

    def etsi_seuraavat(self, alkuosa):
        if not self.todennakoisyydet_laskettu:
            self.laske_todennakoisyydet()

        solmu = self.juuri
        
        for x in alkuosa:
            if x not in solmu.lapset:
                return []
            solmu = solmu.lapset[x]

        vaihtoehdot = []
        for x, lapsi in solmu.lapset.items():
            vaihtoehdot.append((lapsi.todennakoisyys, x))
        return sorted(vaihtoehdot, reverse=True)
