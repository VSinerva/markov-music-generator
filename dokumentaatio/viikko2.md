# Viikkoraportti 2
Perehdyin trie-tietorakenteen teoriaan ja toteutukseen. Punnitsin eri vaihtoehtoja solmun lasten tallentamiselle. Löytämäni python-toteutukset tallensivat lapsisolmut dict-rakenteeseen, mutta se ei vaikuttanut minusta parhaalta vaihtoehdolta tässä tapauksessa. Hajautustaulun sijaan voimme käyttää suoraan taulukkoa, kunhan meillä on jokin tapa muuntaa merkit taulukon indekseiksi. Siirrän tämän laskennan tietorakenteen ulkopuolelle. Toisin sanoen opetusdatan prosessoinnissa ja markovin ketjun tulosteen tulkinnassa muunnan dataa nuoteista indekseiksi ja toisin päin. Tämän voi toteuttaa hajautustaululla tai jollakin muulla tavalla. Oleellisesti tämä tehdään kerran jokaista OPETUSDATAN nuottia kohden, eikä useita kertoja jokaista markovin ketjun iteraatiota kohden. Tietorakenteen käyttö hankaloituu, mutta mielestäni se on tässä projektissa hyväksyttävä kompromissi, sillä tavoitteena ei ole tehdä yleiseen käyttöön tarkoitettua kirjastoa, eikä python olisikaan tehokkain tapa toteuttaa sellaista. Tähän ratkaisuun toivoisin palautetta viikkopalautteessa.

Aikaa käytin tällä viikolla noin 3,5h.