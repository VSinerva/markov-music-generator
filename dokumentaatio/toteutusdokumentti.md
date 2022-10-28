# Toteutusdokumentti

## Ohjelman rakenne hierarkkisessa järjestyksessä
`trie` tarjoaa  nimenomaan Markovin ketjuja varten toteuttamani trien luokkana.

`markov_ketju` sisältää kaikki tarvittavat funktiot itse Markovin ketjuja varten yhtenä luokkana. Hyödyntää `trie`-moduulia.

`midi_kasittelija` hoitaa MIDI-tiedostojen lukemisen ja kirjoittamisen. Ei riipu edellisistä.

`musiikki-generaattori` hyödyntää kaikkia edellä mainittuja moduuleja ja toteuttaa niiden avulla varsinaisen toiminnallisuuden.

`ui` toimii käyttöliittymänä `musiikki-generaattori`-moduulin käyttämiseksi, eikä sisällä varsinaista logiikkaa. Syötteiden validointi tapahtuu täällä.

`main` ei tee muuta kuin käynnistä `ui`:n.

## Aika- ja tilavaativuudet
Tässä tapauksessa käytännössä on kyse vain Trien oikeellisuudesta. Käytetyt trien operaatiot ovat niin yksinkertaisia, että oikeellisuuden tarkistaminen on helppoa. [Viikon 2](https://github.com/ArcticCoder/markov-music-generator/blob/main/dokumentaatio/viikko2.md) raportissa esitellyistä syistä trien solmut hyödyntävät hajautustauluja lapsisolmujen tallentamisessa, jolloin pahimman tapauksen aikavaativuus on itseasiassa O(nm), jossa n on lisättävän/etsittävän merkkijonon pituus ja m on keskimääräinen lapsisolmujen määrä. Kuitenkin keskimääräisessä tapauksessa tämä ei hajautustaulujen kanssa yleensä toteudu, vaan pääsemme lähelle Trien operaatioiden ideaalista O(n) aikavaativuutta.

Toteutunut tilavaativuus vastaa ideaalista O(n), joka on myös helppo todeta koodista. Trie sisältää vain solmuja, joista jokainen sisältää kaksi lukua ja tiedon lapsisolmuista. Luvut vievät tilaa O(n), kun n on solmujen määrä. Jokainen solmu on vain yhden solmun lapsi, jolloin jokainen solmu ilmenee kerran lapsisolmuna. Hajautustaulun tilavaativuus on O(n), jolloin lapsisolmujen tallentamiseen menee yhteensä tilaa O(n). Näin ollen tilavaativuus on O(n).

## Puutteet ja parannusehdotukset
- Ohjelma ei tällä hetkellä anna valita mitään muuta kuin C-duuri sävellajin, eikä molli sävellajeja tueta ollenkaan.
- Rytmin generoimiseen voisi olla useampia menetelmiä.
- Tapa jolla toteutin komennot ei ole erityisen mielekäs omasta mielestäni, sillä sopivan kirjaimen löytäminen kävi jo nyt välillä hankalaksi. Ohjelman merkittävä laajentaminen olisi siis tältä osin turhan hankalaa.
- Alkuosan ja rytmin määrittäminen on hieman kömpelöä merkkijonoissa olevien erikoismerkkien takia.
- Olisin halunnut, että ohjelma kertoo esimerkiksi prosenttina, kuinka monen nuotin kohdalla oli enemmän kuin yksi vaihtoehto. Tämä auttaisi asteen valinnassa, sillä käyttäjä näkisi milloin aletaan käytännössä vain toistamaan opetusdataa sellaisenaan.
- MIDI-muunnos jättää esimerkiksi vanhat sävellaji yms. merkinnät, jotka eivät enää pidä paikkansa. Ei haittaa ohjelman toimintaa, mutta mikäli MIDI-tiedostoista tehtäisiin suoraan partituuri, sävellaji merkittäisiin väärin. Itse nuottien arvot ovat kuitenkin oikein, jolloin ohjelmisto osaa kyllä soittaa oikeat nuotit tästä virheestä riippumatta

## Lähteet
[Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)

[Wikipedia: Markov chain](https://en.wikipedia.org/wiki/Markov_chain)

[Albert Au Yeung "Implementing Trie in Python" (Luettu 15.09.2022)](https://albertauyeung.github.io/2020/06/15/python-trie.html/#implementing-trie-in-python-1)

[Vijaykrishna Ram "Trie Data Structure in C/C++" (Luettu 15.09.2022)](https://www.digitalocean.com/community/tutorials/trie-data-structure-in-c-plus-plus)

[Musescore (opetusdata)](https://musescore.com/sheetmusic?instrument=2&instrumentation=114&license=to_share&recording_type=public-domain)
