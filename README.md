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

![Aanmaken van een speler met gebruikersnaam 'player1', email 'player1@test.com', geboortedatum '12 december 2003', en wachtwoord 'pass1'. Land wordt niet meegegeven want dit is niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/59ec5f26-c91f-4a0d-ad31-d5b63283fbd3)

Het is niet mogelijk om een speler aan te maken met dezelf gebruikersnaam of email. Als dit toch gebeurt, zal het programma een foutmelding teruggeven dat specifieerd wat er mis is.

<img width="966" alt="Aanmaken van een speler met een al bestaand email." src="https://github.com/wobr53/apidev-project/assets/113974538/ffd17404-a74c-4ffe-ae04-77e823fe7579">

<img width="966" alt="Aanmaken van een speler met een al bestaande gebruikersnaam." src="https://github.com/wobr53/apidev-project/assets/113974538/5d68d09b-8e30-467c-87f1-ec528aee1461">

### POST /games
Naast spelers kan je ook spelletjes toevoegen aan de databank. Dit kan met behulp van het post /games endpoint.

![Aanmaken van een spel titel 'Game1', publicatiedatum '8 april 2023', en genre 'RPG'. Genre en ontwikkelaar zijn niet verplicht.](https://github.com/wobr53/apidev-project/assets/113974538/87042d6f-bc64-4d46-ad1a-4a0428920524)

Bij games geldt er ook een restrictie op duplicaten: spelen met de dezelfde titel en publicatiedatum zullen niet worden aangenomen. Een titel kan wel twee keer voorkomen in de databank, maar dan met een verschillende publicatiedatum en vice versa.

<img width="966" alt="Aanmaken van spel met bestaande titel op overeenkomstige publicatiedatum." src="https://github.com/wobr53/apidev-project/assets/113974538/1b86732c-f9a7-4588-ac05-daef1a06f98d">

<img width="966" alt="Aanmaken van spel met onbestaande titel op een al bestaande publicatiedatum." src="https://github.com/wobr53/apidev-project/assets/113974538/eec9a3da-e544-4bcc-bf50-aa638126c560">

### POST /progress
Als laatste kan je ook progressie toevoegen aan de databank. Deze moet echter altijd gekoppeld zijn aan een bestaande speler en game, anders zal de endpoint aangeven welke van de twee niet inorde is.

<img width="966" alt="Aanmaken van progressie met een ongeldige player_id." src="https://github.com/wobr53/apidev-project/assets/113974538/fc05bad5-4763-47e4-94a9-d82678070ad7">

![image](https://github.com/wobr53/apidev-project/assets/113974538/f87d5fd7-85e8-4865-bc29-65b2d98c69fe)

<img width="966" alt="Aanmaken van progressie met een ongeldige game_id." src="https://github.com/wobr53/apidev-project/assets/113974538/1c103209-ea7c-44d7-8a3c-8f4a8afb2f51">

<img width="966" alt="Aanmaken van progressie voor speler 1 in spel 1. Andere parameters zijn niet verplicht." src="https://github.com/wobr53/apidev-project/assets/113974538/50ab5cae-c6a1-49fc-bf61-7d636c44b266">

### POST /token
Zoals je kan zien in de eerste printscreen is er een authenticatiefunctie. Deze zorgt ervoor dat sommige acties in de interface enkel mogelijk zijn als je geauthenticeerd bent tegenover de API.

<img width="966" alt="Authenticatie tegenover de API met de gegevens van speler 1." src="https://github.com/wobr53/apidev-project/assets/113974538/0038c99b-fc16-4007-bd14-b3be64350e68">

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
