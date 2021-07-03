# ml-ops
ML recommendation and prediction model for Top European football leagues

# Motivation
I have been a football fan for almost 15 years now. The one thing that I have experienced from watching and analysing so many matches over the years, is that no matter what players a team has, or the form they have been playing with, on a given day, the result is truly unpredictable. Yes, the team with better team chemistry and talent will always have the higher odds but what transpires in the 90 minutes is all that matters. Factors like how cohesive is the team, how many touches did the top players have, the formation, line up, the intention, winning duels, shots on goal, injuries, luck and many more, are simply volatile and too erratic to predict on any given day.

I have been a Barcelona supporter since 2005 and lately the team has been throwing games left and right with few good spells in between. 
I could see that certain formations, player positions, combinations were really affecting the way the team played. There are ML models online that calculate the odds, expected goals, probability of winning based on few factors, but is there a better way of putting some order into this chaos that we love. 

Do the individual performances and stats only mean something if they are in the right setting? e,g, the lineup, formation, minutes played, games played, teammates, mistakes, duels won and lost, attempts at goal, or just luck. 

The players play a huge role in winning games but a better team doesn't necessarily win against a weak team on a given day. That would make the game really boring. So if any team can win on a given day, why do past stats and performances even matter ? Why do teams want best players to play for them ? What makes a team better than other teams ? How does a weak team win against a better team ? is it always luck or is there something more ?

This motivated me to take a stab at trying to predict the outcome of a game based off of real time stats of players. The model will learn the outcome of games based off of only the individual stats of players in different positions. 

# Challenges

## Getting the data for training:

The first obvious challenge was getting a dataset that contained individual player stats of games from various european leagues. I managed to get a paid subscription from Rotowire where I can get players stats data from all games played in europe from Season 2016 to 2020. The data is available in a csv format that can be downloaded directly from the website. But the problem was the data gave cumulative stats of players for one season. For our use case, we are trying to find out how individual player stats affect the outcome of a given match. So I had to write a data extraction code that downloads the csv reports for individual match days and saves them in a given location. 

## Player positions and their respective stats

The next challenge didn't surface till I started deciding the feature set of my data. My initial plan was to select relevant player stats for a given position ( e.g. saves for gk, shots for fw, ball recoveries for def etc ) and feed them into the model. This would result in a mismatch of fetures in a single dataset. Having different features for different pplayer positions would result in multiple dataset or one dataset with a lot of empty/ null values. I could substitute irrelevant features with 'NA' string but I wasn't too keen on that idea. So I decided to collect all 87 stats for every position on the field and merge them all to form one dataset.

## Getting real time data

After a lot of searching and struggle, I figured that getting real time data to match the training set was going to be a tasking and lengthy job. There are websites where I can webscrap real time stats to collect the data, but while thinking about that, I was able to come up with 2 more use cases that are more immediate and practical. 

One of the use cases was the ability to find similar players to the ones that you are most interested in. e.g. you might want to find a player similar to a quick winger, maybe someone with many dribbles completed and high number of crosses. What if a model can recommend top 5 similar players. This might be useful to uncover players that might be similar in ways than we realize. This use case doesn't need real time data.

Another use case is solely related to scoring, expected goals from individual players based on their real time stats. This is similar to our final use case, which is predicting the winner based on individual stats. Only the target variable will change between these two use cases. 
