# Viikkoraportti 5

Toteutin tällä viikolla toisen kurssilaisen projektin vertaisarvioinnin ja toteutin vertaisarvioinnissa saamiani ehdotuksia. Kirjoitin ohjeita niin ohjelmaan, opetusdataan ja tuotettuihin melodioihin liittyen. Lisäksi selvitin käyttämäni datan lisenssit niin, että pystyin lisäämään MIDI-tiedostot suoraan repositorioon. Generoin kattavan .pylintrc-konfiguraatiotiedoston ja paransin MIDI-käsittelijän testausta. Tämän myötä huomasin ja korjasin ohjelmointi virheen kyseisessä moduulissa. Lisäksi paransin syötteiden validointia.

Varsinainen toiminnallisuus edistyi tällä viikolla sen verran, että ohjelmalle voi määrittää mielivaltaisen rytmin, jota toistetaan tarvittava määrä. Esimerkiksi merkkijono "1/4|1/4|1/2" johtaa siihen, että lopullisessa tiedostossa on aina kaksi neljäsosanuottia ja niiden jälkeen puolinuotti.

Seuraavalla viikolla jatkan erilaisten rytmingenerointi järjestelmien testaamista ja toteuttamista.

Tässä vielä esimerkkinä tämän viikon ohjelmistolla generoitu [melodia.](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-rytmi-aste11.mp3)

Aikaa käytin tällä viikolla noin 12h.
