# import my data 
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamclutch	

# retrieve the clutch stats for the 23-24 szn
clutch_stats = leaguedashteamclutch.LeagueDashTeamClutch(
    season="2023-24",
    season_type_all_star="Regular Season",
    clutch_time="Last 5 Minutes",
    ahead_behind="Ahead or Behind",
    point_diff="5"
)



'''
Algo for determining the champion will take 4 catagories into account
1. Effective field goal EFg = ((2*FGM +1.5*3PM)/FGA): 40%
2. Defensive rating: 30%
3. To % lower the better: 20%
3. +/-: 10%
'''

