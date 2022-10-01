# Testausdokumentti

## Koodin testaus

### Testien toteutus
Automaattinen yksikkötestaus on toteutettu pytest-kirjastolla ja testikattavuuden raportoinnin hoitaa coverage-kirjasto.

### Ohjeet
Ennen testien suorittamista tulee pytest- ja coverage-kirjastot olla asennettuna käytössä olevassa ympäristössä. Testit saa suoritettua kommennolla

`pytest src`

projektin juurikansiosta. Testikattavuusraportin voi luoda juurikansiosta komennolla

` coverage run --branch -m pytest src && coverage html`

Tämän jälkeen raportti löytyy tiedostosta `htmlcov/index.html`.

![Testikattavuusraportti. Kokonaiskattavuus 93%](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/kattavuus.png?raw=true)

## Subjektiivinen testaus
Generoin koodin nykyisellä versiolla 4:nnen asteen Markovin ketjulla lyhyen melodian. Vertailukohtana generoin täysin sattumanvaraisen melodian. Mielestäni ero on huomattava, varsinkin kun otetaan huomioon Markovin ketjujen yksinkertaisuus.

[Markovin ketju](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi1-aste4.mp3)

[Sattuma](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/testi-sattuma.mp3)
