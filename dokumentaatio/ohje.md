# Asentaminen
Vaihtoehtoisesti voi luoda virtuaaliympäristön ennen asennusta. Tämä on vahvasti suositeltavaa, sillä näin projektin vaatimat kirjastot pysyvät erillään muusta järjestelmästä. Virtuaaliympäristön voi luoda esimerkiksi `venv`-nimiseen kansioon projektin juureen komennolla

`python3 -m venv venv`

Tämän jälkeen ympäristön saa käytöön komennolla

`source venv/bin/activate`

Ohjelman vaatimat kirjastot voi asentaa komennolla

`pip install -r requirements.txt`

Ohjelma on nyt valmis käytettäväksi.

# Opetusdata
Opetusdataksi kelpaa mikä tahansa MIDI-tiedosto, mutta itse olen käyttänyt MuseScore-palvelua tietyillä [hakukriteereillä](https://musescore.com/sheetmusic?instrument=2&instrumentation=114&license=to_share&recording_type=public-domain). Ainoa rajoitus on se, että ohjelma jättää huomiotta molli-sävellajeissa (minor key signature) olevat osat. Laadun parantamiseksi jokaisessa MIDI-tiedoston raidassa ("track") olisi hyvä olla vain yksi melodia. Edellä olevasta linkistä löytyvät tiedostot ovat olleet sopivia, joten se on varma valinta, jos olet epävarma.

# MIDI-tiedostojen toistaminen
Monet ohjelmat kykenevät toistamaan MIDI-tiedostoja. Esimerkiksi Windows media player, Totem ja VLC (lisäosilla). Näihin löytyy monia yksinkertaisia ohjeita netistä, joten en selosta tässä enempää.
