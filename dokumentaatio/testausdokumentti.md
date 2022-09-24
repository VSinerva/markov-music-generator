# Testausdokumentti

## Testien toteutus
Automaattinen yksikkötestaus on toteutettu pytest-kirjastolla ja testikattavuuden raportoinnin hoitaa coverage-kirjasto.

## Ohjeet
Ennen testien suorittamista tulee pytest- ja coverage-kirjastot olla asennettuna käytössä olevassa ympäristössä. Testit saa suoritettua kommennolla

`pytest src`

projektin juurikansiosta. Testikattavuusraportin voi luoda juurikansiosta komennolla

` coverage run --branch -m pytest src && coverage html`

Tämän jälkeen raportti löytyy tiedostosta `htmlcov/index.html`.

![Testikattavuusraportti. Kokonaiskattavuus 99%](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/kattavuus.png?raw=true)
