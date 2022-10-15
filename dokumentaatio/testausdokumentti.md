# Testausdokumentti

## Koodin testaus

### Testien toteutus
Automaattinen yksikkötestaus on toteutettu pytest-kirjastolla ja testikattavuuden raportoinnin hoitaa coverage-kirjasto. Aiheen kannalta keskeistä subjektiivista testausta olen toteuttanut generoimalla melodioita ohjelman avulla.

### Ohjeet
Ennen testien suorittamista tulee pytest- ja coverage-kirjastot olla asennettuna käytössä olevassa ympäristössä. Testit saa suoritettua kommennolla

`invoke test`

projektin juurikansiosta. Testikattavuusraportin voi luoda juurikansiosta komennolla

`invoke coverage-report`

Tämän jälkeen raportti löytyy tiedostosta `htmlcov/index.html`.

![Testikattavuusraportti. Kokonaiskattavuus 99%](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/kattavuus.png?raw=true)

Koodin laadun automaattinen "testaus" on toteutettu pylintillä:
`invoke lint`

## Subjektiivinen testaus
Viikko 4: Generoin koodin nykyisellä versiolla 4:nnen asteen Markovin ketjulla lyhyen melodian. Vertailukohtana generoin täysin sattumanvaraisen melodian. Mielestäni ero on huomattava, varsinkin kun otetaan huomioon Markovin ketjujen yksinkertaisuus.

Viikko 5: Toteutin tällä viikolla manuaalisen rytmin määrittämisen. Generoin 80 lyhyen melodian yksinkertaisella kahden tahdin välein toistuvalla rytmillä. Yllätin siitä kuinka paljon yksinkertainenkin rytmi "elävöitti" generoitua melodiaa.

Viikko 6: Testasin tällä viikolla kattavammin eri asteilla. Rajoitin asteen alle 5, sillä huomasin että tätä suuremmilla asteilla monessa tilanteessa oli vain yksi vaihtoehto seuraavalle nuotille, joka viittaa siihen että opetusdatan määrä ei ole riittävän suuri. Poistin myös tämän takia aiemmat testit. Lisäksi toteutin mekanismin, jolla olemassaolevan MIDI tiedoston 1. raidan nuotin voidaan korvata Markovin ketjun antamilla nuoteilla. Nämä "muunnokset" löytyvät myös alta. Näissä oli käytössä 4. asteen ketju.

[Aste 1](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_1.mp3)

[Aste 2](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_2.mp3)

[Aste 3](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_3.mp3)

[Aste 4](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_4.mp3)

[Aste 4, ei rytmiä](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/aste_4_rytmiton.mp3)

[MIDI muunnos 1](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/muunnos1.mp3)

[MIDI muunnos 2](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/muunnos2.mp3)

[Sattuma](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-sattuma.mp3)
