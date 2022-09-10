# Määrittelydokumentti

## Kielet
Toteutan projektin Pythonilla. Lisäksi voin vertaisarvioida C++:lla toteutetun projektin. Dokumentaation kielenä toimii suomi.

## Projekti
Tarkoituksena on tuotaa Markovin ketjujen avulla muusikkia generoiva ohjelma. Markovin ketjuilla saadaan yksinkertaisella oppivalla mallilla tuloksia, jotka noudattavat tiettyjä musiikin lainalaisuuksia ja siten muistuttavat jossain määrin musiikkia. Markovin ketjujen toteuttamiseksi toteutan myös trie-tietorakenteen, joka soveltuu erityisen hyvin esimerkiksi. merkkikolmikoiden määrien tallentamiseen. En ole aiemmin käyttänyt kyseistä rakennetta, enkä Markovin ketjuja, ja valitsin aiheen osittain tästä syystä. Varsinaisen ohjelman ytimen lisäksi joudun opettelemaan paljon uutta liittyen mm. opetusdatan esikäsittelyyn ja lukemiseen.

## Syötteet
Alustavana suunnitelmana ohjelman toimintaa säädellään käynnistysparametreillä. Koulutusdatan lisäksi ohjelmalle syötetään Markovin ketjun aste ja sitä vastaava määrä ensimmäisiä nuotteja. Ohjelma laskee koulutusdatasta Markovin ketjujen astetta vastaavien nuottiryhmien yleisyydet, ja generoi näiden perusteella nuotteja, käyttäen pohjana annettuja ensimmäisiä nuotteja.

## Aika- ja tilavaativuudet
Trie-tietorakenteen tässä projektissa tarvittavien operaatioiden aikavaativuudet ovat O(n), jossa n on etsittävän, lisättävän tai päivitettävän ryhmän pituus. Tämä johtuu siitä, että trie-rakenteessa tiedämme aina oikean seuraavan haaran, ja puun haaran syvyys vastaa suoraan ryhmän pituutta. Eli siis 3 pituista ryhmää vastaava solmu löytyy aina syvyydeltä 3. Search-operaation tilavaativuus on O(1), sillä puuta käsitellään juuresta lähtien solmu kerrallaan, eika suorituksen aikana tallenneta uutta tietoa. Insert-operaatio vie tilaa O(n), sillä voimme joutua tallentamaan uuden solmun jokaista ryhmän merkkiä kohden.

Seuraavan nuotin luominen Markovin ketjulla vaatii kaikkien mahdollisten seuraavien nuottien todennäköisyydet, joten sen aikavaativuus on O(n+m), jossa m on mahdollisten nuottien määrä, ja n on ketjun aste eli ryhmän pituus. Kaikki todennäköisyydet löytyvät samasta trien haarasta, viimeistä merkkiä lukuunottamatta, joten oikean haaran löytämiseen kuluu aikaa O(n), jonka jälkeen luemme todennäköisyydet ajassa O(m). Tilankäyttö riippuu suoraan mahdollisten nuottien määrästä, eli tilavaativuus on O(m).

## Lähteet (Tähän asti)
[Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)

## Muuta
Kuulun TKT kandidaatin opinto-ohjelmaan.
