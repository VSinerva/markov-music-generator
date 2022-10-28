# Asentaminen
Lataa repositorio `git clone`-komennolla tai [releases](https://github.com/ArcticCoder/markov-music-generator/releases)-osiosta

Halutessasi voit luoda virtuaaliympäristön ennen asennusta. Tämä on vahvasti suositeltavaa, sillä näin projektin vaatimat kirjastot pysyvät erillään muusta järjestelmästä. Virtuaaliympäristön voi luoda esimerkiksi `venv`-nimiseen kansioon projektin juureen komennolla

`python3 -m venv venv`

Tämän jälkeen ympäristön saa käytöön komennolla

`source venv/bin/activate`

Ohjelman vaatimat kirjastot voi asentaa komennolla

`pip install -r requirements.txt`

Ohjelma on nyt valmis käytettäväksi

`invoke start`

Ohjelma tulostaa ohjeet komennolla 'A'. Tässä vielä tarkentavaa tietoa komennoista, joiden kohdalla se on mielekästä:
## (O)petusdata
Opetusdatan tiedosto polku. Voi olla absoluuttinen tai suhteellinen. Hyväksyy esimerkiksi ns. wildcard merkin * ja käsittelee sitä yleisellä tavalla.  Taustalla on pythonin [glob](https://docs.python.org/3/library/glob.html), jonka dokumentaatiosta löytyy enemmän tietoa siitä, mitä merkkejä voi käyttää ja miten. Muutujan oletusarvo ottaa opetusdataksi kaikki "opetusdata"-kansion MIDI-tiedostot.

## a(L)kuosa
Generoitavan sävelmän alkuosa. Esitetään perinteisillä nuottimerkinnöillä, kuten "C4" ja "D#5". Erottimena toimii `|`. Mikäli alkuosan pituus ylittää Markovin ketjun asteen, ylimääräiset nuotit EIVÄT PÄÄDY lopulliseen melodiaan, vaan ne jätetään huomiotta. Toisaalta mikäli alkuosan pituus on pienempi kuin Markovin ketjun aste, sitä täydennetään opetusdatan perusteella riittävän pitkäksi.

## (R)ytmi
Aseta rytmi nuottien kestoina. Esim neljäsosanuotti "1/4", puolinuotti "1/2" ja kokonainen nuotti "1". Erottimena toimii `|`. Rytmiä käytetään annetussa järjestyksessä ja toistetaan alusta alkaen tarpeen mukaan.

## (M)uunnettava MIDI
Vaihtoehtoinen tapa määrittää rytmi, tempo ja muita musikaalisia piirteitä. Tässä tilassa ohjelma ottaa annetun MIDI-tiedoston ja luo siitä kopion kahdella muutoksella
- Keston yläraja määräytyy generoitavien nuottien määrästä
- Sävelkorkeudet vaihdetaan Markovin ketjulla generoituihin
- Vain ensimmäinen raita (track) säilyy, muut hävitetään
Kaikki muut ominaisuudet, kuten rytmi, tempo, kuinka kovaa nuotteja soitetaan, montako nuottia soi kerralla jne. säilyvät ennallaan.

# Opetusdatan hankinta
Opetusdataksi kelpaa mikä tahansa MIDI-tiedosto, mutta itse olen käyttänyt MuseScore-palvelua tietyillä [hakukriteereillä](https://musescore.com/sheetmusic?instrument=2&instrumentation=114&license=to_share&recording_type=public-domain). Ainoa rajoitus on se, että ohjelma jättää huomiotta molli-sävellajeissa (minor key signature) olevat osat. Laadun parantamiseksi jokaisessa MIDI-tiedoston raidassa ("track") olisi hyvä olla vain yksi melodia. Edellä olevasta linkistä löytyvät tiedostot ovat olleet sopivia, joten se on varma valinta, jos olet epävarma. Repositoriossa on myös valmiiksi opetusdataa.

# MIDI-tiedostojen toistaminen
Monet ohjelmat kykenevät toistamaan MIDI-tiedostoja. Esimerkiksi Windows media player, Totem ja VLC (lisäosilla). Näihin löytyy monia yksinkertaisia ohjeita netistä, joten en selosta tässä enempää.
