# Testausdokumentti

## Koodin testaus

### Testien toteutus
Automaattinen yksikkötestaus on toteutettu pytest-kirjastolla ja testikattavuuden raportoinnin hoitaa coverage-kirjasto. Aiheen kannalta keskeistä subjektiivista testausta olen toteuttanut generoimalla manuaalisesti melodioita ohjelman avulla. Koodin laadun automaattinen "testaus" on toteutettu pylintillä.

### Ohjeet
Ennen testien suorittamista tulee pytest- ja coverage-kirjastot olla asennettuna käytössä olevassa ympäristössä (löytyvät jo, mikäli [asennusohjeita](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/ohje.md#asentaminen) on noudatettu). Testit saa suoritettua kommennolla

`invoke test`

projektin juurikansiosta. Testikattavuusraportin voi luoda juurikansiosta komennolla

`invoke coverage-report`

Tämän jälkeen raportti löytyy tiedostosta `htmlcov/index.html`.

![Testikattavuusraportti. Kokonaiskattavuus 99%](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/kattavuus.png?raw=true)

Pylint tarkistuksen voi suorittaa komennolla

`invoke lint`

### Mitä yksikkötestit (pääpiirtein) kattavat
Ohjeiden mukaisesti `main` ja `ui` on jätetty testien ulkopuolelle.

`trie`:
- Triee:n tulee lisättyä kaikki mitä pitää, ja laskuri toimii oikein yksinkertaisella testitapauksella
- Triestä ei löydy sellaista, mitä ei pitäisi. Tarkistettu tietyt rajatut tilanteet, eli jos syötetään "AB", niin trien juuren lapsista ei löydy "B", ja toisaalta "A"-solmun laskuri on 0
- Trie laskee ja antaa todennäköisyydet oikein yksinkertaisella esimerkkitapauksella

`markov_ketju`:
- Virheidenkäsittely antamalla vriheellisiä arvoja
- Ketju antaa oikean sekvenssin, niin yhdellä kuin kahdella asteella, kun seuraavia merkkejä on vain yksi mahdollinen
- Ketju toimii oikein, kun opetusdatassa on useampi lista, eikä esimerkiksi yhdistä listoja
- Ketju palauttaa `None`, jos vaihtoehtoja ei ole
- Tarkistettu, että 3000 generoidun merkin osuudet vastaavat likimain (5 prosenttiyksikön marginaali) opetusdatasta nähtäviä oikeita osuuksia

`midi_kasittelija`:
- Vastaus vastaa syötettä, kun kirjoitetaan ja sitten luetaan tietty nuottilista
- Kun toetutetaan muunnos annetulle tiedostolle, tiedostosta löytyy oikeat nuotit, eikä muita nuotteja. Tämän enempää muunnoksen oikeellisuutta ei tarkisteta. Tätä varten loin erillisien testi MIDI-tiedoston
- Molli-sävellajissa olevat nuotit jätetään oikein pois kokonaan, ja muut trasponoidaan C-duuriin. Tätä varten loin erillisien testi MIDI-tiedoston

`musiikki_generaattori`:
Yksi iso testi, jossa
- Kirjoitetaan tietyt nuotit MIDI-tiedostoon
- Luetaan tämä tiedosto opetusdatana. Opetusdatassa jokaiselle nuotille tai nuottiparille on vain yksi mahdollinen seuraava nuotti
- Tarkistetaan, että 1. asteen ketju antaa oikean sekvenssin
- Tarkistetaan, että 2. asteen ketju antaa oikean sekvenssin
- Tarkistetaan, että nuotteja ei generoida, mikäli alkuosalle ei löydy sopivaa jatkoa opetusdatasta

## Subjektiivinen testaus
Subjektiivista testausta varten keräsin opetusdataa ja generoin eri asetuksilla sävelmiä. Alla on:
- Eri asteisilla ketjuilla generoituja, yksinkertaista rytmiä noudattavia melodioita
- Rytmitön 4. asteen ketjulla tuotettu
- Kaksi MIDI muunnosta 4. asteen ketjuilla
- Täysin sattumanvaraisia nuotteja sisältävä rytmitön "melodia" ikään kuin lähtökohtana

Itse en huomannut juurikaan eroa 1. ja toisen 2. asteen ketjujen välillä. Molemmat olivat merkittävä parannus sattumaan nähden, mutta melko "päättömän" oloisia kuitenkin. 3. asteen ketju oli kenties hieman parempi, mutta mielestäni 4. asteen ketju oli yllättävän suuri parannus aiempiin nähden. Tätä pidemmillä ketjuilla päädyttäisiin enimmäkseen toistamaan opetusdataa, joten niitä ei tässä ole.

Yllätyin erityisesti siitä, kuinka suuri rytmin merkitys on. Vertaamalla yksinkertaista rytmiä tasaiseen rytmiin, ja toisaalta oikeiden sävelmien rytmeihin, huomataan että rytmitön musiikki on hyvinkin raskasta kuunneltavaa, mutta toisaalta jo neljännen asteen Markovin ketjulla saatiin yllättävän musikaalisia lopputuloksia, kun rytmi kopioitiin oikeasta sävelmästä (MIDI-muunnos).

[Aste 1](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_1.mp3)

[Aste 2](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_2.mp3)

[Aste 3](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_3.mp3)

[Aste 4](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_4.mp3)

[Aste 4, ei rytmiä](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_4_rytmiton.mp3)

[MIDI muunnos 1](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/muunnos1.mp3)

[MIDI muunnos 2](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/muunnos2.mp3)

[Sattuma](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-sattuma.mp3)
