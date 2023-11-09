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
Als laatste kan je ook progress toevoegen aan de databank. Deze moet echter altijd gekoppeld zijn aan een bestaande speler en game, anders zal de endpoint aangeven welke van de twee niet inorde is.

![Aanmaken van progress met een ongeldige player_id.](https://github.com/wobr53/apidev-project/assets/113974538/8051b3f4-719a-44ea-a137-c95c0f0fc86a)

![Aanmaken van progress met een ongeldige game_id.](https://github.com/wobr53/apidev-project/assets/113974538/5016afdd-e7e8-4873-af7e-1c460acf884f)

![Aanmaken van progress voor speler 1 in spel 1. Andere parameters zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/82015ee0-0047-4ef8-994f-7cdfabea6631)

### POST /token
Zoals je kan zien in de eerste printscreen is er een authenticatiefunctie. Deze zorgt ervoor dat sommige acties in de interface enkel mogelijk zijn als je geauthenticeerd bent tegenover de API.

![Authenticatie tegenover de API met de gegevens van speler 1.](https://github.com/wobr53/apidev-project/assets/113974538/6592c34b-8305-42e3-b303-fb549ba181e7)

In de printscreen kan je zien dat speler 1 nu een sessietoken heeft gekregen. Hij is nu gemachtigd om versleutelde endpoints te gebruiken.

>[!NOTE]
> Voor demonstratie-doeleinden heb ik 'off screen' een paar extra spelers, spelen, en progress-vermeldingen toegevoegd aan de databank.



