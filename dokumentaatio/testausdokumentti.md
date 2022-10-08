# Testausdokumentti

## Koodin testaus

### Testien toteutus
Automaattinen yksikkötestaus on toteutettu pytest-kirjastolla ja testikattavuuden raportoinnin hoitaa coverage-kirjasto. Aiheen kannalta keskeistä subjektiivista testausta olen toteuttanut generoimalla melodioita ohjelman avulla.

### Ohjeet
Ennen testien suorittamista tulee pytest- ja coverage-kirjastot olla asennettuna käytössä olevassa ympäristössä. Testit saa suoritettua kommennolla

`pytest src`

projektin juurikansiosta. Testikattavuusraportin voi luoda juurikansiosta komennolla

` coverage run --branch -m pytest src && coverage html`

Tämän jälkeen raportti löytyy tiedostosta `htmlcov/index.html`.

![Testikattavuusraportti. Kokonaiskattavuus 99%](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/kattavuus.png?raw=true)

## Subjektiivinen testaus
Viikko 4: Generoin koodin nykyisellä versiolla 4:nnen asteen Markovin ketjulla lyhyen melodian. Vertailukohtana generoin täysin sattumanvaraisen melodian. Mielestäni ero on huomattava, varsinkin kun otetaan huomioon Markovin ketjujen yksinkertaisuus.

Viikko 5: Toteutin tällä viikolla manuaalisen rytmin määrittämisen. Generoin 80 lyhyen melodian yksinkertaisella kahden tahdin välein toistuvalla rytmillä. Yllätin siitä kuinka paljon yksinkertainenkin rytmi "elävöitti" generoitua melodiaa.

[Viikko 4](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi1-aste4.mp3)

[Viikko 5](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-rytmi-aste11.mp3)

[Sattuma](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-sattuma.mp3)
