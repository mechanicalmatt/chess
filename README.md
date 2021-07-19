MVP:
-   player mentions @chess_bot and the bot replies with their stats

MVP BREAKDOWN:
-   fetch player data
--      1. rank in each game type (D, B, R, B)

####

FURTHER FEATURES:
 
give more detail on a profile
--      analyze fav openings
--      matplotlib charts/graphs on their history
basic statistics
player comparison
--      x vs. y: win/lose odds
--      rankings

####

make the usability as simple as possible - very simple formatting
**      stats "username"
**      daily stats "username"
**      rapid stats "username"
**      ...

####

INTERACTIONS:

how to tell if tweet has already been replied to:
>  have a doc with every replied to tweet
>>  open and read doc, see if most recent tweet is in this doc
>>> if recent_id not in doc: break; else: fulfill request