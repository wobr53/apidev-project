# Basisproject API Development

Link to API: https://project-api-service-wobr53.cloud.okteto.net/docs#/

## Thema
Als thema heb ik ervoor gekozen om mijn project te maken rond videospelletjes; meer bepaald de progressie in videospelletjes. Ik ben zelf een gamer en daarbij ook een enorme trophy/achievements - hunter, dus ik dacht dat het wel eens leuk zou zijn om dit stukje van mezelf te kunnen verwerken in een project.

## Werking API
De basis van mijn API ligt aan de onderliggende Sqlite-databank. Deze bevat drie tabellen: Player, Game, en Progress. Hierin kunnen spelers en spelletjes afzonderlijk van elkaar bestaan, maar zal een progressie-vermelding steeds gelinkt zijn aan zowel een speler als een spel.
Er is ook een beknopte webinterface voorzien om te kunnen interageren met de databank.

![Webinterface voor het API basisproject. Gehost op Okteto.](https://github.com/wobr53/apidev-project/assets/113974538/dcdd59f1-e564-4124-b165-23c72b89e731 "Webinterface voor het API basisproject. Gehost op Okteto.")

In wat volgt zal ik over elke functie van de webinterface gaan.

### DELETE /reset
We starten met /reset. Dit endpoint staat ons toe om alle data uit de databank te verwijderen.

>[!NOTE]
>In een API die naar productie gaat, zou je dit endpoint best beveiligen (net zoals alle andere, nu onbeveiligde, enpoints), maar voor demonstratie-redenen heb ik dit niet gedaan.

![Delete all in werking.](https://github.com/wobr53/apidev-project/assets/113974538/5c2d856c-3006-4eea-ab5a-f41dcda476df "Delete all in werking.")

Na het opvragen van dit request zal alle data uit de databank verwijderd zijn. Het request laat zijn werking zien door achteraf een 'detail' terug te sturen.

### POST /players
Deze request zal een nieuwe speler aanmaken mits je de juiste request body meegeeft.

![Aanmaken van een speler met gebruikersnaam 'player1', email 'player1@test.com', geboortedatum '12 december 2003', en wachtwoord 'pass1'. Land wordt niet meegegeven want dit is niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/c6b727ef-add5-4153-b276-3ea2384a9e76 "Aanmaken van een speler met gebruikersnaam 'player1', email 'player1@test.com', geboortedatum '12 december 2003', en wachtwoord 'pass1'. Land wordt niet meegegeven want dit is niet verplicht.")

Het is niet mogelijk om een speler aan te maken met dezelf gebruikersnaam of email. Als dit toch gebeurt, zal het programma een foutmelding teruggeven dat specifieerd wat er mis is.

![Aanmaken van een speler met een al bestaand email.](https://github.com/wobr53/apidev-project/assets/113974538/c4fa03fd-805a-49ac-86d7-8d8f3f80669d "Aanmaken van een speler met een al bestaand email.")

![Aanmaken van een speler met een al bestaande gebruikersnaam.](https://github.com/wobr53/apidev-project/assets/113974538/f3d9230c-f968-4dee-a59f-7d4bb520ff04 "Aanmaken van een speler met een al bestaande gebruikersnaam.")

### POST /games
Naast spelers kan je ook spelletjes toevoegen aan de databank. Dit kan met behulp van het post /games endpoint.

![Aanmaken van een spel titel 'Game1', publicatiedatum '8 april 2023', en genre 'RPG'. Genre en ontwikkelaar zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/f30f3ec1-29d5-4904-872e-750cf917e33e "Aanmaken van een spel titel 'Game1', publicatiedatum '8 april 2023', en genre 'RPG'. Genre en ontwikkelaar zijn niet verplicht.")

Bij games geldt er ook een restrictie op duplicaten: spelen met de dezelfde titel en publicatiedatum zullen niet worden aangenomen. Een titel kan wel twee keer voorkomen in de databank, maar dan met een verschillende publicatiedatum en vice versa.

![Aanmaken van spel met bestaande titel op overeenkomstige publicatiedatum.](https://github.com/wobr53/apidev-project/assets/113974538/80380d03-ef8d-46ac-8d1c-911fb3f603d9 "Aanmaken van spel met bestaande titel op overeenkomstige publicatiedatum.")

![Aanmaken van spel met onbestaande titel op een al bestaande publicatiedatum.](https://github.com/wobr53/apidev-project/assets/113974538/e07d140e-35a5-43b7-9c14-31d1eb7a6aa2 "Aanmaken van spel met onbestaande titel op een al bestaande publicatiedatum.")

### POST /progress
Als laatste kan je ook progressie toevoegen aan de databank. Deze moet echter altijd gekoppeld zijn aan een bestaande speler en game, anders zal de endpoint aangeven welke van de twee niet inorde is.

![Aanmaken van progressie met een ongeldige player_id.](https://github.com/wobr53/apidev-project/assets/113974538/f8509f83-1581-4f08-bd31-555a399cf363 "Aanmaken van progressie met een ongeldige player_id.")

![Aanmaken van progressie met een ongeldige game_id.](https://github.com/wobr53/apidev-project/assets/113974538/16916a11-1d29-436a-ba14-60be417532e1 "Aanmaken van progressie met een ongeldige game_id.")

![Aanmaken van progressie voor speler 1 in spel 1. Andere parameters zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/d3b362b7-bbe8-433d-9a1d-a2592e66d48c "Aanmaken van progressie voor speler 1 in spel 1. Andere parameters zijn niet verplicht.")

### POST /token
Zoals je kan zien in de eerste printscreen is er een authenticatiefunctie. Deze zorgt ervoor dat sommige acties in de interface enkel mogelijk zijn als je geauthenticeerd bent tegenover de API.

![Authenticatie tegenover de API met de gegevens van speler 1.](https://github.com/wobr53/apidev-project/assets/113974538/b7378185-0f03-4a82-8a6e-502ba3790a69 "Authenticatie tegenover de API met de gegevens van speler 1.")

In de printscreen kan je zien dat speler 1 nu een sessietoken heeft gekregen. Hij is nu gemachtigd om versleutelde endpoints te gebruiken.

>[!NOTE]
> Voor demonstratie-doeleinden heb ik 'off screen' een paar extra spelers, spelen, en progress-vermeldingen toegevoegd aan de databank.

>[!IMPORTANT]
>Na het vergaren van de accesstoken moet je hem meegeven in het authorisation veld van het request.
>![Access token in authorization veld.](https://github.com/wobr53/apidev-project/assets/113974538/3d8b7c0a-78c7-48cb-baf1-cc6c930649b2 "Access token in authorization veld.")

### GET /players
Met dit get request vragen we alle spelers met overeenkomstige progress uit de databank op. Indien er geen spelers in de databank zitten, krijg je een lege lijst terug.

![Alle spelers 1/4](https://github.com/wobr53/apidev-project/assets/113974538/4ea2a032-ec0e-4944-aef4-9fcfd74f85f8 "Alle spelers 1/4")
![Alle spelers 2/4](https://github.com/wobr53/apidev-project/assets/113974538/bac47735-f11e-4d97-9b22-106597cc6f0d "Alle spelers 2/4")
![Alle spelers 3/4](https://github.com/wobr53/apidev-project/assets/113974538/4d8f7a9d-c82b-4acd-b2fc-249040cb3f98 "Alle spelers 3/4")
![Alle spelers 4/4](https://github.com/wobr53/apidev-project/assets/113974538/a63a5af0-c739-49d1-abad-f3391876aeb4 "Alle spelers 4/4")

### GET /games
Dit is hetzelfde als voor de spelers maar dan voor spelletjes.

![Alle spelen 1/4](https://github.com/wobr53/apidev-project/assets/113974538/17c255ae-d039-4af6-958f-82e6a809197f "Alle spelen 1/4")
![Alle spelen 2/4](https://github.com/wobr53/apidev-project/assets/113974538/99872ef4-daf5-4102-9632-bd072d40b985 "Alle spelen 2/4")
![Alle spelen 3/4](https://github.com/wobr53/apidev-project/assets/113974538/4faf5cc1-f44b-4548-8199-c431c5e37d09 "Alle spelen 3/4")
![Alle spelen 4/4](https://github.com/wobr53/apidev-project/assets/113974538/eb57e565-e879-42ec-a388-db21df6f3487 "Alle spelen 4/4")

### GET /progress
Met dit request vragen we elke progressie-vermelding afzonderlijk op. Ook hier zal je een lege lijst krijgen als er geen progressie-vermeldingen zijn.

![Alle progressie 1/3](https://github.com/wobr53/apidev-project/assets/113974538/95d9b01c-9b98-47c4-b26e-21afd2050285 "Alle progressie 1/3")
![Alle progressie 2/3](https://github.com/wobr53/apidev-project/assets/113974538/ec67054a-a758-428f-8075-c0f2c345c912 "Alle progressie 2/3")
![Alle progressie 3/3](https://github.com/wobr53/apidev-project/assets/113974538/029251fb-7267-454a-9658-4a9f36ba24e3 "Alle prgressie 3/3")

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
