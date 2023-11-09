# Basisproject API Development

## Thema
Als thema heb ik ervoor gekozen om mijn project te maken rond videospelletjes; meer bepaald de progressie in videospelletjes. Ik ben zelf een gamer en daarbij ook een enorme trophy/achievements - hunter, dus ik dacht dat het wel eens leuk zou zijn om dit stukje van mezelf te kunnen verwerken in een project.

## Werking API
De basis van mijn API ligt aan de onderliggende Sqlite-databank. Deze bevat drie tabellen: Player, Game, en Progress. Hierin kunnen spelers en spelletjes afzonderlijk van elkaar bestaan, maar zal een progressie-vermelding steeds gelinkt zijn aan zowel een speler als een spel.
Er is ook een beknopte webinterface voorzien om te kunnen interageren met de databank.

![Webinterface voor het API basisproject. Gehost op Okteto.](https://github.com/wobr53/apidev-project/assets/113974538/0e64a8e7-892e-43a3-9974-17384d04025f)

In wat volgt zal ik over elke functie van de webinterface gaan.

### DELETE /reset
We starten met /reset. Dit endpoint staat ons toe om alle data uit de databank te verwijderen.

>[!NOTE]
>In een API die naar productie gaat, zou je dit endpoint best beveiligen (net zoals alle andere, nu onbeveiligde, enpoints), maar voor demonstratie-redenen heb ik dit niet gedaan.

![Delete all in werking.](https://github.com/wobr53/apidev-project/assets/113974538/486790b6-e3ce-4690-88a0-0f892e4c1b9c)

Na het opvragen van dit request zal alle data uit de databank verwijderd zijn. Het request laat zijn werking zien door achteraf een 'detail' terug te sturen.

### POST /players
Deze request zal een nieuwe speler aanmaken mits je de juiste request body meegeeft.

![Aanmaken van een speler met gebruikersnaam "player1", email "player1@test.com", geboortedatum "12 december 2003", en wachtwoord "pass1". Land wordt niet meegegeven want dit is niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/793f5c76-def1-45d2-a042-1d0c2ee437d5)

Het is niet mogelijk om een speler aan te maken met dezelf gebruikersnaam of email. Als dit toch gebeurt, zal het programma een foutmelding teruggeven dat specifieerd wat er mis is.

![Aanmaken van een speler met een al bestaand email.](https://github.com/wobr53/apidev-project/assets/113974538/b556597e-2053-4b00-b748-ebedf305f390)

![Aanmaken van een speler met een al bestaande gebruikersnaam.](https://github.com/wobr53/apidev-project/assets/113974538/6f2da4d6-862f-4ba0-8530-2f36224b0098)

### POST /games
Naast spelers kan je ook spelletjes toevoegen aan de databank. Dit kan met behulp van het post /games endpoint.

![Aanmaken van een spel titel "Game1", publicatiedatum "8 april 2023", en genre "RPG". Genre en ontwikkelaar zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/46b27e38-9ecc-46dc-9e68-1c76b8f9922a)

Bij games geldt er ook een restrictie op duplicaten: spelen met de dezelfde titel en publicatiedatum zullen niet worden aangenomen. Een titel kan wel twee keer voorkomen in de databank, maar dan met een verschillende publicatiedatum en vice versa.

![Aanmaken van spel met bestaande titel op overeenkomstige publicatiedatum.](https://github.com/wobr53/apidev-project/assets/113974538/6e7e2014-1584-4405-aa5c-1cce6f593d49)

![Aanmaken van spel met onbestaande titel op een al bestaande publicatiedatum.](https://github.com/wobr53/apidev-project/assets/113974538/604d34d0-a294-4c83-92e7-88bf4b180185)

![Aanmaken van spel met bestaande titel op een niet overeenkomende publicatiedatum.](https://github.com/wobr53/apidev-project/assets/113974538/886a733f-9295-4e19-acd9-1faa34b743aa)

### POST /progress
Als laatste kan je ook progressie toevoegen aan de databank. Deze moet echter altijd gekoppeld zijn aan een bestaande speler en game, anders zal de endpoint aangeven welke van de twee niet inorde is.

![Aanmaken van progressie met een ongeldige player_id.](https://github.com/wobr53/apidev-project/assets/113974538/8051b3f4-719a-44ea-a137-c95c0f0fc86a)

![Aanmaken van progressie met een ongeldige game_id.](https://github.com/wobr53/apidev-project/assets/113974538/5016afdd-e7e8-4873-af7e-1c460acf884f)

![Aanmaken van progressie voor speler 1 in spel 1. Andere parameters zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/82015ee0-0047-4ef8-994f-7cdfabea6631)

### POST /token
Zoals je kan zien in de eerste printscreen is er een authenticatiefunctie. Deze zorgt ervoor dat sommige acties in de interface enkel mogelijk zijn als je geauthenticeerd bent tegenover de API.

![Authenticatie tegenover de API met de gegevens van speler 1.](https://github.com/wobr53/apidev-project/assets/113974538/6592c34b-8305-42e3-b303-fb549ba181e7)

In de printscreen kan je zien dat speler 1 nu een sessietoken heeft gekregen. Hij is nu gemachtigd om versleutelde endpoints te gebruiken.

>[!NOTE]
> Voor demonstratie-doeleinden heb ik 'off screen' een paar extra spelers, spelen, en progress-vermeldingen toegevoegd aan de databank.

>[!IMPORTANT]
>Na het vergaren van de accesstoken moet je hem meegeven in het authorisation veld van het request.
>![Access token in authorization veld.](https://github.com/wobr53/apidev-project/assets/113974538/30d9e319-9130-402f-98fc-a498efc22b54)

### GET /players
Met dit get request vragen we alle spelers met overeenkomstige progress uit de databank op. Indien er geen spelers in de databank zitten, krijg je een lege lijst terug.

![Alle spelers 1/4](https://github.com/wobr53/apidev-project/assets/113974538/ad118f57-9327-4212-a26d-4eadfe1b852d)
![Alle spelers 2/4](https://github.com/wobr53/apidev-project/assets/113974538/eba865ce-6241-443f-a232-372d65bdb762)
![Alle spelers 3/4](https://github.com/wobr53/apidev-project/assets/113974538/f0641aa7-8f80-44a7-9b74-709f526b7f95)
![Alle spelers 4/4](https://github.com/wobr53/apidev-project/assets/113974538/69d430ef-8822-493e-9cfa-9bc2e003d925)

### GET /games
Dit is hetzelfde als voor de spelers maar dan voor spelletjes.

![Alle spelen 1/4](https://github.com/wobr53/apidev-project/assets/113974538/d09173d8-3ef3-4b59-be9a-643d5ce69be0)
![Alle spelen 2/4](https://github.com/wobr53/apidev-project/assets/113974538/7f472eae-528a-473d-bfe9-a1a22328f618)
![Alle spelen 3/4](https://github.com/wobr53/apidev-project/assets/113974538/1db1a3e6-2804-44e8-bcc6-05e8e57bcada)
![Alle spelen 4/4](https://github.com/wobr53/apidev-project/assets/113974538/8dd77244-14b7-4690-a8ec-9f13ee8b66d9)

### GET /progress
Met dit request vragen we elke progressie-vermelding afzonderlijk op. Ook hier zal je een lege lijst krijgen als er geen progressie-vermeldingen zijn.

![Alle progressie 1/3](https://github.com/wobr53/apidev-project/assets/113974538/501a2703-8d71-409a-b430-da5ff523a38d)
![Alle progressie 2/3](https://github.com/wobr53/apidev-project/assets/113974538/3fe2cee9-9fb8-44b1-83f4-92fc1704741a)
![Alle prgressie 3/3](https://github.com/wobr53/apidev-project/assets/113974538/6d91a839-4327-4079-92d9-045d66be7e60)

### GET players/{username}
Dit request zal je de speler zijn/haar gegevens en statistieken laten zien op basis van de gebruikersnaam. Als de gebruikersnaam niet bestaat krijg je dit ook te weten.

![Gegevens en statistieken van speler met gebruikersnaam "player3".](https://github.com/wobr53/apidev-project/assets/113974538/5cd80a5d-5194-4b85-baeb-066b015d3fca)
![Ongeldige gebruikersnaam meegegeven.](https://github.com/wobr53/apidev-project/assets/113974538/67f26815-b9d7-4414-ad95-6808b2f2bb62)

### PUT /progress?player=&game=
Als er progressie in de databank staat die achterhaald is, kan je deze updaten met dit request. 
Er zijn wel drie vereisten:
+ De speler moet bestaan in de databank
+ Het spel moet bestaan in de databank
+ Er moet al een progressie-vermelding voor die/dat speler en spel in de databank bestaan
Als aan één van deze vereisten niet voldaan is, krijg je een gepaste foutmelding terug.

![Update van progressie voor onbestaande speler.](https://github.com/wobr53/apidev-project/assets/113974538/a608dc0e-94f8-4f4a-a215-08f482508147)
![Update van progressie voor onbestaand spel.](https://github.com/wobr53/apidev-project/assets/113974538/9a0bf83f-f99b-4af0-842f-17df29793c1f)
![Update van progressie voor onbestaande progressie.](https://github.com/wobr53/apidev-project/assets/113974538/d914332c-0dd2-4fa6-9fba-a73f5ce030ba)
![Update van progressie voor speler 2 in spel 3.](https://github.com/wobr53/apidev-project/assets/113974538/5e00c990-6fd0-4dfb-b6db-d277c4e9d0d1)

Zoals je zal zien is de progressie-vermelding voor speler 2 in spel 3 nu veranderd.

![Verificatie wijziging](https://github.com/wobr53/apidev-project/assets/113974538/3e1e38c6-7719-4f96-8e12-6cb30986d8aa)


### DELETE /progress?player=&game=
Je kan ook specifieke progressie-vermeldingen uit de databank verwijderen.
Hier zijn ook weer drie vereisten van toepassing:
+ De speler moet bestaan in de databank
+ Het spel moet bestaan in de databank
+ Er moet al een progressie-vermelding voor die/dat speler en spel in de databank bestaan

![Delete van progressie van onbestaande speler.](https://github.com/wobr53/apidev-project/assets/113974538/635d7b7f-8c06-4517-a895-a3bd08ba5f7b)
![Delete van progressie van onbestaand spel.](https://github.com/wobr53/apidev-project/assets/113974538/2734bbf0-2419-4a15-a1ef-08060a6e6264)
![Delete van progressie bij onbestaande progressie.](https://github.com/wobr53/apidev-project/assets/113974538/75388f0a-09e4-4f05-bd0e-4d21b15ebdc1)
![Delete van progressie van speler 3 in spel 3.](https://github.com/wobr53/apidev-project/assets/113974538/ae1e829e-911a-4a20-be6b-cb29c6209328)

Nu zal je zien dat de progressie volledig is verwijderd uit de databank.

![Verificatie verwijdering](https://github.com/wobr53/apidev-project/assets/113974538/d7b4bc51-78f2-48f4-9cf7-98b6ea198cfe)
