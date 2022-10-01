# Toteutusdokumentti

## Ohjelman rakenne
Ohjelman ytimessä ovat `trie` ja `markov_ketju` moduulit, jotka toteuttavat varsinaiset tietorakenteet ja keskeisimmät algoritmit. `midi_kasittelija` hoitaa MIDI-tiedostojen lukemisen ja kirjoittamisen. `musiikki-generaattori` hyödyntää kaikkia edellä mainittuja moduuleja ja toteuttaa niiden avulla varsinaisen toiminnallisuuden. `ui` toimii käyttöliittymänä `musiikki-generaattori`-moduulin käyttämiseksi.

## Aika- ja tilavaativuudet
Nähdäkseni saavutin määrittelydokumentissa asetetun tavoitteet aika- ja tilavaativuuksien suhteen.

## Lähteet
[Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)

[Wikipedia: Markov chain](https://en.wikipedia.org/wiki/Markov_chain)

[Albert Au Yeung "Implementing Trie in Python" (Luettu 15.09.2022)](https://albertauyeung.github.io/2020/06/15/python-trie.html/#implementing-trie-in-python-1)

[Vijaykrishna Ram "Trie Data Structure in C/C++" (Luettu 15.09.2022)](https://www.digitalocean.com/community/tutorials/trie-data-structure-in-c-plus-plus)
