# Waifu dataset

Extract from `waifus.json`:
```json
[
{
    "age": null, 
    "alternative_name": "\u7d50\u57ce \u660e\u65e5\u5948", 
    "birthday_day": 30, 
    "birthday_month": "September", 
    "birthday_year": "", 
    "blood_type": "", 
    "bust": "82.00", 
    "creator": {
        "id": 42, 
        "name": "Railtracks", 
        "rolename": ""
    }, 
    "creator_id": 42, 
    "description": "Asuna is a friend of Kirito and is a sub-leader of the guild Knights of the Blood (KoB), a medium-sized guild of about thirty players, also called the strongest guild in Aincrad. Being one of the few girls that are in SAO, and even more so that she's extremely pretty, she receives many invitations and proposals. She is a skilled player earning the title \"Lightning Flash\" for her extraordinary skill with the sword. Her game alias is the same as her real world name.\r\n\r\nFR: Asuna, de son vrai de son vrai nom Asuna Y\u00fbki, est une joueuse de 17 ans tr\u00e8s peu exp\u00e9riment\u00e9e en mati\u00e8re de jeu vid\u00e9o. Et pour dire, Sword art Online est son premier jeu vid\u00e9o car \u00e0 la base elle trouve que ceux-ci ne sont qu'une perte de temps.", 
    "display_picture": "https://mywaifulist.s3-us-west-1.amazonaws.com/waifus/58/7e0fdce769d88cfa0adda64a09bf0b84940d5574329c71122ea3eaf4a45d94e2.jpeg", 
    "height": "168.00", 
    "hip": "83.00", 
    "id": 58, 
    "likes": 1442, 
    "name": "Yuuki Asuna", 
    "origin": "Japan", 
    "series": {
        "description": "In 2022, a virtual reality massively multiplayer online role-playing game (VRMMORPG) called Sword Art Online (SAO) is released. With the NerveGear, a helmet that stimulates the user's five senses via their brain, players can experience and control their in-game characters with their minds. Both the game and the NerveGear was created by Akihiko Kayaba.\r\n\r\nOn November 6, 10,000 players log into the SAO's mainframe cyberspace for the first time, only to discover that they are unable to log out. Kayaba appears and tells the players that they must beat all 100 floors of Aincrad, a steel castle which is the setting of SAO, if they wish to be free. Those who suffer in-game deaths or forcibly remove the NerveGear out-of-game will suffer real-life deaths.\r\n\r\nThe main character, Kirigaya \"Kirito\" Kazuto, was also one of 1,000 testers in the game's previous closed beta. With the advantage of previous VR gaming experience and a drive to protect other beta testers from discrimination, he isolates himself from the greater group and plays the game alone, bearing the mantle of \"beater\", a \"beta tester\" and \"cheater\". As the players progress through the game Kirito eventually befriends a young girl named Asuna Yuuki, who form a relationship that later turns into in-game marriage. After the duo discover that Akihiko Kayaba was playing the game as the leader of the guild Asuna joined, they confront and destroy him, freeing themselves and the other players from the game.", 
        "id": 49, 
        "name": "Sword Art Online", 
        "slug": "sword-art-online"
    }, 
    "slug": "yuuki-asuna", 
    "tags": [
        {
            "id": 1869, 
            "name": "worst anime"
        }, 
        {
            "id": 1870, 
            "name": "trash"
        }, 
        {
            "id": 1927, 
            "name": "idiot"
        }
    ], 
    "trash": 2093, 
    "waist": "60.00", 
    "weight": "55.00"
},
]
```

## Build the dataset

### Install
```
pip install -r requirements.txt
```

### Get the data
```
python scrapper.py
```

All the scrapped data will be stored in `waifus.json`

## Sources
All the data and images come from [MyWaifuList](https://mywaifulist.moe)
