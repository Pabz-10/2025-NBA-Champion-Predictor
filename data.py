# import my data 
import pandas as pd
from nba_api.stats.endpoints import leaguedashteamclutch	

# retrieve the clutch stats for the 23-24 szn
clutch_stats = leaguedashteamclutch.LeagueDashTeamClutch(
    season="2023-24",
    season_type_all_star="Playoffs",
    clutch_time="Last 5 Minutes",
    ahead_behind="Ahead or Behind",
    point_diff="5"  
)

#create a df for the stats and save as csv file
clutch_stats_df = clutch_stats.get_data_frames()[0]
clutch_stats_df.to_csv('clutch_stats.csv', index=False)
nba_data = pd.read_csv('clutch_stats.csv')
nba_data.head()

'''
Algo for determining the champion will take 4 catagories into account
1. Effective field goal eFG = ((2*FGM +1.5*3PM)/FGA): 40%
2. Defensive rating: 30%
3. defensive rebounds: 20%
4. TO% lower the better: 10%
'''
# Grab our values 
nba_data["eFG"] = ((2 *nba_data["FGM"] + 1.5 * nba_data["FG3M"]) / nba_data["FGA"])
nba_data["Def_Rtg"] = nba_data["DEF_RTG"]
nba_data["DREB"] = nba_data["DREB"]
nba_data['TO%'] = nba_data['TOV']

#Get our decile values
nba_data["eFG_decile"] = pd.qcut(nba_data["eFG"], 10, labels=False, duplicates="drop") + 1
nba_data["Def_Rtg_decile"] = pd.qcut(nba_data["Def_Rtg"], 10, labels=False, duplicates="drop") + 1
nba_data["DREB_decile"] = pd.qcut(nba_data["DREB"], 10, labels=False, duplicates="drop") + 1
nba_data["TO%_decile"] = pd.qcut(nba_data["TO%"], 10, labels=False, duplicates="drop") + 1

#Pop these values into my algo
nba_data["Finals"] = (
    (0.4 * nba_data["eFG_decile"]) +
    (0.3 * nba_data["Def_Rtg_decile"]) +
    (0.2 * nba_data["DREB_decile"]) -
    (0.1 * nba_data['TO%_decile'])
    )

# Sort the data to see my top teams
nba_data = nba_data.sort_values(by="Finals", ascending=False)
print(nba_data[['TEAM_NAME', 'Finals']].head())

