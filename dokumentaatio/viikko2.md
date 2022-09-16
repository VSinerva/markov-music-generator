# Viikkoraportti 2
Perehdyin trie-tietorakenteen teoriaan ja toteutukseen. Punnitsin eri vaihtoehtoja solmun lasten tallentamiselle. Löytämäni python-toteutukset tallensivat lapsisolmut dict-rakenteeseen. Hajautustaulun sijaan voimme käyttää suoraan taulukkoa, kunhan meillä on jokin tapa muuntaa merkit taulukon indekseiksi. Taulukon nopeus tässä tapauksessa riippuu vahvasti indeksien saamisen nopeudesta, enkä löytänyt tapaa tehdä tätä pythonissa niin, että kokonaisuus olisi nopeampi kuin hajautustaulu niillä aakkoston suuruksilla, joita tässä projektissa tullaan käyttämään. Esimerkiksi C++ tukee suoraan merkin ASCII-koodin ja kokonaislukujen välisen erotuksen laskemista, joka olisi laskennallisesti erittäin nopeaa, mutta pythonissa tähän tarvitaan ord()-funktio. Ord-funktio ja taulukko olivat testeissäni hitaampia kuin hajautustaulu. Hajautustaulun käyttäminen myös tuo helppoutta ja joustavuutta rakenteen käyttöön, sillä trie ei näin ota kantaa siihen, mitä siihen voidaan tallentaa. Tähän ratkaisuun toivoisin palautetta viikkopalautteessa.

Toinen poikkeama löytämästäni kirjallisuudesta on solmuissa oleva sanan loppua merkkaava muuttuja. Tässä käytössä en tarvitse operaatioita, jotka hyödyntäisivät tätä, ja saman toiminnon voin tarvittaessa saavuttaa tarkistamalla onko laskuri > 0.

Lisäsin koodin laadun seuraamista varten pylintin, pytestin ja coveragen projektiin. Korjasin pylintin havaitsemat puutteet koodissa. Kirjoitin yksikkötestis trie-moduulilleni. Coverage-moduulilla saa tehtyä kattavuusraportin, tämänhetkinen haarakattavuus on 100%.

Seuraavalla viikolla toteutan itse Markovin ketjut ja testaan niitä jonkinlaisella keinotekoisella opetusdatalla. Ajan riittäessä aloitan myös varsinaisen musiikin käsittelyn toteuttamisen.

Aikaa käytin tällä viikolla noin 7h.
