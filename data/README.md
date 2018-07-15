# Data

This repository contains data required to analyze the libraries of members of the [ResetEra](https://steamcommunity.com/groups/ResetEra/) Steam group.

## List of members ##

A sample of 1000 Steam-ID of members of this group can be parsed from the following URL:
```https://steamcommunity.com/groups/ResetEra/memberslistxml/?xml=1&p=1```

To build an exhaustive list of members, you will need to:
- iterate over the page numbers (parameter ```&p=```) of the group,
- aggregate the samples of 1000 Steam-ID,
- remove any  duplicate Steam-ID, for instance using [Notepadd++](https://stackoverflow.com/a/3958364) or Python directly.

## Steam API key ##

To access the libary of a Steam user, you will need your private API key, which can be found at:
```https://steamcommunity.com/dev/apikey```

## Steam library ##

The most recently played games of a user with Steam-ID STEAMID are available at:
```https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/?key=MYAPIKEY&steamid=STEAMID```

The Steam library of a user with Steam-ID STEAMID are available at:
```https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=MYAPIKEY&steamid=STEAMID```

The Steam library, without free-to-play games, of a user with Steam-ID STEAMID are available at:
```https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key=MYAPIKEY&steamid=STEAMID&include_played_free_games=0```
