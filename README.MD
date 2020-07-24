## Thema generator

### Vereisten:
- Een werkende lokale ssh key (hiermee wordt de git repo opgehaald)

### Ondersteuning voor:
- bitbucket en github repos
- https://github.com/creativetimofficial/material-dashboard
- https://github.com/creativetimofficial/argon-design-system
- https://github.com/creativetimofficial/blk-design-system


### Clone deze repo lokaal en maak in de root een .env bestand aan met de onderstaande inhoud:
```
GIT_REPO=https://github.com/creativetimofficial/material-dashboard.git
BRAND_PRIMARY=#073997
BRAND_INFO=#057270
BRAND_SUCCESS=#28832e
BRAND_WARNING=#e28e0c
BRAND_DANGER=#ac2c15
BRAND_ROSE=#893092
BRAND_INVERSE=#082532
```

Voer hierna een ```docker-compose up -d``` uit.

Er wordt een container gemaakt waarin een simpele webserver draait. Hierin is het thema nog zonder de aanpassingen te bekijken.
- [localhost:8080](http://localhost:8080)

Voer hierna onderstaand commando uit om het thema aan te passen en om hiervan een zip file te maken. Deze is daarna te vinden in de map: /dest
- ```docker-compose exec app python3 create_template.py```

Er zijn een aantal acties die uitgevoerd kunnen worden, default wordt alles uitgevoerd.
- clone git repo van de template
- create-css (de kleuren worden in een colors.json bestand gezet en toegepast op het thema)
- create-zip (de bestanden worden in een zip file gezet in de /dest folder)

### Losse acties:
#### Om de kleuren tussentijds aan te passen kan is het mogelijk om het bestand colors.json aan te passen:
- /src/colors.json (deze is tijdens de eerste run gemaakt)
- Voer hierna: ```docker-compose exec app python3 create_template.py create-css``` uit. Dit past de CSS aan met de aangepaste waardes.

#### Om na een aanpassing een nieuwe zip file te maken kan je onderstaande uitvoeren:
- ```docker-compose exec app python3 create_template.py create-zip```

