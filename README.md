# Overview 
After watching team USA win the gold medal at the olympics this summer I was left without any basketball to watch and so I decided to create a fun project that combined my love of hoops with programming. Thus my NBA champion predictor was born. 
This program fetchs data from the nba api and saves it to a CSV file. The data is then analyzed and the 2 finalist teams are predicted based on the algorithm i devised below.

# Data Set & Algorithm  
The data set I used in this program only took into account 2024 playoff data from clutch time which is defined as "the final five minutes of the fourth quarter or overtime when the score is within five points" by the NBA. My choice to use this particular data set was due to the fact that the level of play in the NBA only goes up as the playoffs progress and often times the game is won or lost during this clutch period. 

With the data chosen, my next step was to devise an algorithm that could take this data and predict two teams to make it to the finals. To do this, my alogrithim took into account four key catagories:
- Effective Field Goal Percentage (eFG%): weighted at 40%
  
- Defensive Rating per 100 possesions: weighted at 30%
  
- Total Rebounds (REB): weighted at 20%
  
- Turnover Percentage (TO%): weighted at 10%

The eFG% gives us an adjusted field goal percentage that takes into account three point shots, this stats is weighted the highest at 40%. 
My reasoning for the high weight is that games are won by the team that scores the most points and teams that have a higher eFG% will score more points.

Defensive rating was weighted the second highest due to the fact that teams with high defensive ratings will limit opponents from scoring thus giving up less points. 
On top of this games are often decided by who can make a stop when the game is on the line. 

Total Rebounds was weighted at 20% as while not as impactful as the previous two catagories, teams the get more rebounds will get more chances to score the ball, simple as that.

The final catagory weighted at 10% was turnover percentage, as teams with a lower TO% give up the ball less, and thus get more opportunities to score. 

When running the program, the algorithm states that the 2025 NBA finals will be between the Denver Nuggets and the Milwaukee Bucks, with the 
Nuggest coming out on top!

# Features 
- Clutch Stats Analysis: Uses NBA clutch stats like Effective Field Goal Percentage, Defensive Rating, Total Rebounds, and Turnover Percentage.
  
- Weighted Algorithm: Combines statistical categories with custom weightings to predict the likelihood of an NBA team maing the finals and becoming the champion.
  
- Decile-Based Scoring: Converts the stats into deciles for better normalization.
  
- Data from NBA API: Fetches real-time data from the NBA API for analysis.

# Requirements 
- Python 3.1

# Installation
1. First clone the repository
```
git clone https://github.com/Pabz-10/2025-NBA-Champion-Predictor.git
```
2. Install the dependencies via the requirements.txt
```
pip install -r requirements.txt
```
# Usage 
Make sure you're in the home directory and run the program
```
python data.py
```
# License
This project is licensed under the [MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) License.
